
import asyncio
import logging
import os
import struct
from typing import Optional, Tuple

import pyrogram
from pyrogram.crypto import aes
from .tcp import TCP, Proxy

log = logging.getLogger(__name__)

MIN_PACKET_SIZE = 4

_EXT_HDR = b"\x7f"
_SINGLE_BYTE_HEADERS = [bytes([i]) for i in range(128)]

class TCPAbridgedO(TCP):
    """
    MTProto Obfuscated Abridged transport.

    The entire connection (including the abridged length header) is wrapped in
    AES-CTR-256. The cipher keystream is strictly sequential: every byte
    decrypted or encrypted advances the shared IV/state by exactly one block
    position.  Any reordering or interleaving of recv() or send() calls would
    shift the CTR offset, producing garbage on all subsequent packets.

    Fixes applied vs. original:
    1. _recv_lock covers the full multi-step read (header + body) atomically.
    2. send() acquires self.lock for the full encrypt-then-write sequence so
       that concurrent send() calls cannot interleave their CTR keystreams.
    3. readexactly() in the base class eliminates partial-read ambiguity.
    4. Debug logging: payload length, constructor ID, first 16 raw bytes.
    """

    RESERVED = (b"HEAD", b"POST", b"GET ", b"OPTI", b"\xee" * 4)

    def __init__(self, ipv6: bool, proxy: Proxy) -> None:
        super().__init__(ipv6, proxy)
        self.encrypt = None
        self.decrypt = None

    async def connect(self, address: Tuple[str, int]) -> None:
        await super().connect(address)

        while True:
            nonce = bytearray(os.urandom(64))
            if (
                nonce[0] != 0xEF
                and bytes(nonce[:4]) not in self.RESERVED
                and nonce[4:8] != b"\x00" * 4
            ):
                nonce[56] = nonce[57] = nonce[58] = nonce[59] = 0xEF
                break

        temp = bytearray(nonce[55:7:-1])
        self.encrypt = (nonce[8:40], nonce[40:56], bytearray(1))
        self.decrypt = (temp[0:32], temp[32:48], bytearray(1))

        nonce[56:64] = aes.ctr256_encrypt(bytes(nonce), *self.encrypt)[56:64]
        await super().send(bytes(nonce))

    async def send(self, data: bytes, *args) -> None:
        length_in_words = len(data) >> 2  

        if length_in_words <= 126:
            header = _SINGLE_BYTE_HEADERS[length_in_words]
        else:
            header = _EXT_HDR + struct.pack("<I", length_in_words)[:3]

        plaintext = header + data

        loop = asyncio.get_running_loop()
        async with self.lock:
            payload = await loop.run_in_executor(
                pyrogram.crypto_executor,
                aes.ctr256_encrypt,
                plaintext,
                *self.encrypt,
            )
            writer = self.writer
            if writer is None:
                return
            try:
                writer.write(payload)
                if writer.transport.get_write_buffer_size() > 65536:
                    await writer.drain()
            except Exception as exc:
                log.debug("TCPAbridgedO.send error: %s %s", type(exc).__name__, exc)
                raise OSError(exc) from exc

    async def recv(self, length: int = 0) -> Optional[bytes]:
        async with self._recv_lock:
            raw_header = await super().recv(1)
            if raw_header is None:
                return None

            dec_header = aes.ctr256_decrypt(raw_header, *self.decrypt)

            if dec_header == _EXT_HDR:
                raw_ext = await super().recv(3)
                if raw_ext is None:
                    return None
                dec_ext         = aes.ctr256_decrypt(raw_ext, *self.decrypt)
                length_in_words = struct.unpack_from("<I", dec_ext + b"\x00")[0]
            else:
                length_in_words = dec_header[0]

            payload_size = length_in_words << 2  

            if payload_size < MIN_PACKET_SIZE:
                log.warning(
                    "TCPAbridgedO: implausible payload size %d — discarding frame",
                    payload_size,
                )
                return None

            raw_body = await super().recv(payload_size)
            if raw_body is None:
                return None

            data = aes.ctr256_decrypt(raw_body, *self.decrypt)

            constructor = struct.unpack_from("<I", data, 0)[0] if len(data) >= 4 else 0
            log.debug(
                "TCPAbridgedO recv: payload=%d bytes  constructor=0x%08x  head16=%s",
                len(data),
                constructor,
                data[:16].hex(),
            )
            return data
