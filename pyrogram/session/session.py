
import asyncio
import bisect
import logging
import os
import struct
import time
from hashlib import sha1
from io import BytesIO
from typing import Optional

import pyrogram
from pyrogram import raw
from pyrogram.connection import Connection
from pyrogram.crypto import mtproto
from pyrogram.errors import (
    RPCError, InternalServerError, AuthKeyDuplicated,
    FloodWait, FloodPremiumWait,
    ServiceUnavailable, BadMsgNotification,
    SecurityCheckMismatch, Unauthorized
)
from pyrogram.raw.all import layer
from pyrogram.raw.core import TLObject, MsgContainer, Int, FutureSalts
from .internals import MsgId, MsgFactory

log = logging.getLogger(__name__)

_STRUCT_I = struct.Struct("<i")

class Result:
    """Awaitable container for a pending RPC result."""
    __slots__ = ["value", "future"]

    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.value  = None
        self.future: asyncio.Future = loop.create_future()

class Session:
    START_TIMEOUT  = 2
    WAIT_TIMEOUT   = 15
    SLEEP_THRESHOLD = 10
    MAX_RETRIES    = 10
    ACKS_THRESHOLD = 10
    PING_INTERVAL  = 5
    STORED_MSG_IDS_MAX_SIZE = 500

    MAX_DECODE_ERRORS = 3

    BACKOFF_INITIAL    = 1.0
    BACKOFF_MULTIPLIER = 2.0
    BACKOFF_MAX        = 30.0

    TRANSPORT_ERRORS = {
        404: "auth key not found",
        429: "transport flood",
        444: "invalid DC"
    }

    def __init__(
        self,
        client: "pyrogram.Client",
        dc_id: int,
        auth_key: bytes,
        test_mode: bool,
        is_media: bool = False,
        is_cdn: bool = False
    ):
        self.client    = client
        self.dc_id     = dc_id
        self.auth_key  = auth_key
        self.test_mode = test_mode
        self.is_media  = is_media
        self.is_cdn    = is_cdn

        self.connection: Optional[Connection] = None

        self.auth_key_id = sha1(auth_key).digest()[-8:]

        self.session_id  = os.urandom(8)
        self.msg_factory = MsgFactory()

        self.salt = 0

        self.pending_acks: set = set()

        self.results: dict = {}

        self.stored_msg_ids = []

        self.ping_task       = None
        self.ping_task_event = asyncio.Event()

        self.recv_task = None

        self.is_started = asyncio.Event()

        self._restart_lock    = asyncio.Lock()
        self._generation: int = 0
        self._restart_backoff: float = 0.0
        self._decode_error_count: int = 0

    async def start(self):
        while True:
            self.connection = self.client.connection_factory(
                dc_id=self.dc_id,
                test_mode=self.test_mode,
                ipv6=self.client.ipv6,
                alt_port=self.client.alt_port,
                proxy=self.client.proxy,
                media=self.is_media,
                protocol_factory=self.client.protocol_factory
            )

            try:
                await self.connection.connect()

                loop = asyncio.get_running_loop()
                self.recv_task = loop.create_task(self.recv_worker())

                await self.send(raw.functions.Ping(ping_id=0), timeout=self.START_TIMEOUT)

                if not self.is_cdn:
                    await self.send(
                        raw.functions.InvokeWithLayer(
                            layer=layer,
                            query=raw.functions.InitConnection(
                                api_id=await self.client.storage.api_id(),
                                app_version=self.client.app_version,
                                device_model=self.client.device_model,
                                system_version=self.client.system_version,
                                system_lang_code=self.client.system_lang_code,
                                lang_code=self.client.lang_code,
                                lang_pack=self.client.lang_pack,
                                query=raw.functions.help.GetConfig(),
                            )
                        ),
                        timeout=self.START_TIMEOUT
                    )

                self.ping_task = loop.create_task(self.ping_worker())

                log.info("Session initialized: Layer %s", layer)
                log.info("Device: %s - %s", self.client.device_model, self.client.app_version)
                log.info("System: %s (%s)", self.client.system_version, self.client.lang_code)

            except AuthKeyDuplicated as e:
                await self.stop()
                raise e
            except (OSError, RPCError):
                await self.stop()
            except Exception as e:
                await self.stop()
                raise e
            else:
                break

        self._generation        += 1
        self._restart_backoff    = 0.0
        self._decode_error_count = 0
        self.is_started.set()
        log.info("Session started (generation=%d)", self._generation)

    async def stop(self):
        self.is_started.clear()

        self.stored_msg_ids.clear()

        self.ping_task_event.set()

        if self.ping_task is not None:
            self.ping_task.cancel()
            try:
                await self.ping_task
            except (asyncio.CancelledError, Exception):
                pass
            self.ping_task = None

        self.ping_task_event.clear()

        if self.recv_task is not None:
            self.recv_task.cancel()
            try:
                await self.recv_task
            except (asyncio.CancelledError, Exception):
                pass
            self.recv_task = None

        await self.connection.close()

        if not self.is_media and callable(self.client.disconnect_handler):
            try:
                await self.client.disconnect_handler(self.client)
            except Exception as e:
                log.exception(e)

        log.info("Session stopped")

    async def restart(self):
        """Public restart entry-point (called directly, not via _schedule_restart).
        Serialised by _restart_lock; no generation check because the caller
        explicitly requested a restart (e.g. auth.py, test code)."""
        async with self._restart_lock:
            log.info("Session restarting (explicit call)")
            await self.stop()
            await self.start()

    def _schedule_restart(self, reason: str) -> None:
        """
        Schedule a conditional restart.

        Captures the current generation so that the restart task becomes a
        no-op if the session has already been restarted by the time it runs.
        This is the core fix for the sequential restart storm:

            recv_worker  → create_task(restart())   ← fires, session restarts, gen++
            ping_worker  → create_task(restart())   ← stale gen → IGNORED
            handle_packet→ create_task(restart())   ← stale gen → IGNORED
        """
        gen = self._generation
        asyncio.get_running_loop().create_task(
            self._do_scheduled_restart(gen, reason)
        )

    async def _do_scheduled_restart(self, gen: int, reason: str) -> None:
        """
        Execute a scheduled restart only if it is still relevant.

        Relevance rules
        ---------------
        1. Generation match: if start() already ran since this task was
           created, the connection is healthy again — drop the request.
        2. Lock deduplication: if a restart is already running for THIS
           generation, wait for it to complete and then exit; the running
           restart will fix everything.
        3. Double-check after lock: another coroutine may have completed
           between our locked() check and our acquire — recheck generation.
        4. Exponential backoff: applied before stop/start to avoid hammering
           Telegram on persistent network failures.
        """

        if gen != self._generation:
            log.debug(
                "Restart request ignored — stale generation %d (current %d): %s",
                gen, self._generation, reason
            )
            return

        if self._restart_lock.locked():
            log.debug("Restart already in progress, coalescing: %s", reason)
            async with self._restart_lock:
                pass
            return

        async with self._restart_lock:

            if gen != self._generation:
                log.debug(
                    "Restart request obsolete after lock acquisition "
                    "(gen %d → current %d): %s",
                    gen, self._generation, reason
                )
                return

            log.warning("Session restarting — reason: %s (generation %d)", reason, gen)

            if self._restart_backoff > 0:
                log.info(
                    "Restart backoff: waiting %.1f s before reconnecting",
                    self._restart_backoff
                )
                await asyncio.sleep(self._restart_backoff)

            await self.stop()

            try:
                await self.start()

            except Exception as exc:

                self._restart_backoff = min(
                    max(self._restart_backoff, self.BACKOFF_INITIAL) * self.BACKOFF_MULTIPLIER,
                    self.BACKOFF_MAX
                )
                log.error(
                    "Session restart failed: %s  —  next backoff: %.1f s",
                    exc, self._restart_backoff
                )

    async def handle_packet(self, packet):
        loop = asyncio.get_running_loop()
        try:
            data = await loop.run_in_executor(
                pyrogram.crypto_executor,
                mtproto.unpack,
                BytesIO(packet),
                self.session_id,
                self.auth_key,
                self.auth_key_id
            )
        except ValueError as e:

            self._decode_error_count += 1
            log.warning(
                "Packet decode failure #%d/%d: %s",
                self._decode_error_count, self.MAX_DECODE_ERRORS, e
            )
            if self._decode_error_count >= self.MAX_DECODE_ERRORS:
                self._decode_error_count = 0
                self._schedule_restart(
                    f"consecutive decode failures ({self.MAX_DECODE_ERRORS})"
                )
            return

        self._decode_error_count = 0

        messages = (
            data.body.messages
            if isinstance(data.body, MsgContainer)
            else (data,)
        )

        log.debug("Received: %s", data)

        pending_acks    = self.pending_acks
        results         = self.results
        stored_msg_ids  = self.stored_msg_ids
        max_stored      = Session.STORED_MSG_IDS_MAX_SIZE
        MsgId_now       = MsgId

        for msg in messages:
            if msg.seq_no & 1:  
                msg_id = msg.msg_id
                if msg_id in pending_acks:
                    continue
                pending_acks.add(msg_id)

            try:
                if len(stored_msg_ids) > max_stored:
                    del stored_msg_ids[:max_stored >> 1]

                if stored_msg_ids:
                    msg_id = msg.msg_id

                    if msg_id < stored_msg_ids[0]:
                        raise SecurityCheckMismatch(
                            "The msg_id is lower than all the stored values"
                        )

                    if msg_id in stored_msg_ids:
                        raise SecurityCheckMismatch(
                            "The msg_id is equal to any of the stored values"
                        )

                    time_diff = (msg_id - MsgId_now()) / 4294967296  

                    if time_diff > 30:
                        raise SecurityCheckMismatch(
                            "The msg_id belongs to over 30 seconds in the future. "
                            "Most likely the client time has to be synchronized."
                        )

                    if time_diff < -300:
                        raise SecurityCheckMismatch(
                            "The msg_id belongs to over 300 seconds in the past. "
                            "Most likely the client time has to be synchronized."
                        )

            except SecurityCheckMismatch as e:

                log.warning("Security check mismatch: %s — scheduling restart", e)
                self._schedule_restart("security check mismatch")
                return
            else:
                bisect.insort(stored_msg_ids, msg.msg_id)

            body = msg.body
            body_type = type(body)

            if body_type in (raw.types.MsgDetailedInfo, raw.types.MsgNewDetailedInfo):
                pending_acks.add(body.answer_msg_id)
                continue

            if body_type is raw.types.NewSessionCreated:
                continue

            msg_id = None

            if body_type in (raw.types.BadMsgNotification, raw.types.BadServerSalt):
                msg_id = body.bad_msg_id
            elif body_type in (FutureSalts, raw.types.RpcResult):
                msg_id = body.req_msg_id
            elif body_type is raw.types.Pong:
                msg_id = body.msg_id
            else:
                if self.client is not None:
                    loop.create_task(self.client.handle_updates(body))

            if msg_id is not None and msg_id in results:
                result = results[msg_id]
                result.value = getattr(body, "result", body)
                if not result.future.done():
                    result.future.set_result(None)

        if len(pending_acks) >= self.ACKS_THRESHOLD:
            log.debug("Sending %s acks", len(pending_acks))
            try:
                await self.send(raw.types.MsgsAck(msg_ids=list(pending_acks)), False)
            except OSError:
                pass
            else:
                pending_acks.clear()

    async def ping_worker(self):
        log.info("PingTask started")

        while True:
            try:
                await asyncio.wait_for(
                    self.ping_task_event.wait(), self.PING_INTERVAL
                )
            except asyncio.TimeoutError:
                pass
            else:
                break

            try:
                await self.send(
                    raw.functions.PingDelayDisconnect(
                        ping_id=0, disconnect_delay=self.WAIT_TIMEOUT + 10
                    ),
                    False
                )
            except OSError as exc:

                log.warning("PingTask OSError: %s — scheduling reconnect", exc)
                self._schedule_restart(f"ping OSError: {exc}")
                break
            except RPCError:
                pass

        log.info("PingTask stopped")

    async def recv_worker(self):
        log.info("NetworkTask started")

        loop = asyncio.get_running_loop()

        while True:
            packet = await self.connection.recv()

            if packet is None or len(packet) == 4:
                if packet:
                    error_code = -_STRUCT_I.unpack_from(packet)[0]

                    if error_code == 404:
                        raise Unauthorized(
                            "Auth key not found in the system. You must delete "
                            "your session file and log in again with your phone "
                            "number or bot token."
                        )

                    log.warning(
                        "Server sent transport error: %s (%s)",
                        error_code,
                        Session.TRANSPORT_ERRORS.get(error_code, "unknown error")
                    )

                if self.is_started.is_set():
                    reason = (
                        "recv returned None (EOF / connection reset)"
                        if packet is None
                        else f"transport error {-_STRUCT_I.unpack_from(packet)[0]}"
                    )
                    log.warning("NetworkTask: %s", reason)
                    self._schedule_restart(reason)
                else:
                    log.debug(
                        "NetworkTask: recv returned %s but session is stopping — "
                        "no restart scheduled",
                        "None" if packet is None else "transport error"
                    )

                break

            loop.create_task(self.handle_packet(packet))

        log.info("NetworkTask stopped")

    async def send(
        self,
        data: TLObject,
        wait_response: bool = True,
        timeout: float = WAIT_TIMEOUT
    ):
        bad_msg_retries = 2
        loop = asyncio.get_running_loop()

        while True:
            message = self.msg_factory(data)
            msg_id  = message.msg_id

            if wait_response:
                result_obj = Result(loop)
                self.results[msg_id] = result_obj

            log.debug("Sent: %s", message)

            payload = await loop.run_in_executor(
                pyrogram.crypto_executor,
                mtproto.pack,
                message,
                self.salt,
                self.session_id,
                self.auth_key,
                self.auth_key_id
            )

            try:
                await self.connection.send(payload)
            except OSError as e:
                self.results.pop(msg_id, None)
                raise e

            if not wait_response:
                return None

            try:
                await asyncio.wait_for(result_obj.future, timeout)
            except asyncio.TimeoutError:
                pass

            result = self.results.pop(msg_id, None)
            value  = result.value if result is not None else None

            if value is None:
                raise TimeoutError("Request timed out")

            if isinstance(value, raw.types.RpcError):
                inner = data
                if isinstance(
                    inner,
                    (raw.functions.InvokeWithoutUpdates, raw.functions.InvokeWithTakeout)
                ):
                    inner = inner.query
                RPCError.raise_it(value, type(inner))

            if isinstance(value, raw.types.BadMsgNotification):
                bad_msg_retries -= 1
                if bad_msg_retries <= 0:
                    raise BadMsgNotification(value.error_code)
                self._handle_bad_notification()
                continue

            if isinstance(value, raw.types.BadServerSalt):
                self.salt = value.new_server_salt
                continue

            return value

    def _handle_bad_notification(self):
        new_msg_id = MsgId()
        if self.stored_msg_ids and self.stored_msg_ids[-1] >= new_msg_id:
            new_msg_id = self.stored_msg_ids[-1] + 4
            log.debug(
                "Changing msg_id old=%s new=%s",
                self.stored_msg_ids[-1], new_msg_id
            )
        if self.stored_msg_ids:
            self.stored_msg_ids[-1] = new_msg_id

    async def invoke(
        self,
        query: TLObject,
        retries: int = MAX_RETRIES,
        timeout: float = WAIT_TIMEOUT,
        sleep_threshold: float = SLEEP_THRESHOLD
    ):
        try:
            await asyncio.wait_for(self.is_started.wait(), self.WAIT_TIMEOUT)
        except asyncio.TimeoutError:
            pass

        if isinstance(
            query,
            (raw.functions.InvokeWithoutUpdates, raw.functions.InvokeWithTakeout)
        ):
            inner_query = query.query
        else:
            inner_query = query

        query_name = ".".join(inner_query.QUALNAME.split(".")[1:])

        remaining = retries

        while True:
            try:
                return await self.send(query, timeout=timeout)

            except (FloodWait, FloodPremiumWait) as e:
                amount = e.value

                if amount > sleep_threshold >= 0:
                    raise

                log.warning(
                    '[%s] Waiting for %s seconds before continuing (required by "%s")',
                    self.client.name, amount, query_name
                )
                await asyncio.sleep(amount)

            except (OSError, InternalServerError, ServiceUnavailable) as e:
                if remaining == 0:
                    raise e from None

                attempt = retries - remaining + 1
                (log.warning if remaining < 2 else log.info)(
                    '[%s] Retrying "%s" (attempt %d/%d) due to: %s',
                    self.client.name, query_name,
                    attempt, retries,
                    str(e) or repr(e)
                )

                remaining -= 1
                await asyncio.sleep(0.5)
