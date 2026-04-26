
import logging
import os
import struct
from typing import Optional, Tuple

from pyrogram.crypto import aes
from .tcp import TCP, Proxy

log = logging.getLogger(__name__)

MIN_PACKET_SIZE = 4
MAX_PACKET_SIZE = 16 * 1024 * 1024

_STRUCT_I = struct.Struct("<i")
_ZERO_BYTES4 = b"\x00" * 4

class TCPIntermediateO(TCP):
    """
    MTProto Obfuscated Intermediate transport.

    The 4-byte length header and all payload bytes are encrypted with AES-CTR.
    The cipher keystream is sequential — every send() and recv() call must
    process bytes in the exact order they arrive on the wire.

    Fixes applied:
    1. _recv_lock covers header + body atomically.
    2. send() uses a single synchronous encrypt call (no executor needed —
       tgcrypto is already C-fast) followed immediately by the write, keeping
       the CTR state mutation and the write in the same lock window.
    3. Payload-size guard: reject implausible sizes before allocating memory.
    4. Debug logging: payload length, constructor ID, first 16 plaintext bytes.
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
                and nonce[4:8] != _ZERO_BYTES4
            ):
                nonce[56] = nonce[57] = nonce[58] = nonce[59] = 0xEE
                break

        temp = bytearray(nonce[55:7:-1])
        self.encrypt = (nonce[8:40], nonce[40:56], bytearray(1))
        self.decrypt = (temp[0:32], temp[32:48], bytearray(1))

        nonce[56:64] = aes.ctr256_encrypt(bytes(nonce), *self.encrypt)[56:64]
        await super().send(bytes(nonce))

    async def send(self, data: bytes, *args) -> None:
        plaintext = _STRUCT_I.pack(len(data)) + data

        async with self.lock:
            ciphertext = aes.ctr256_encrypt(plaintext, *self.encrypt)
            writer = self.writer
            if writer is None:
                return
            try:
                writer.write(ciphertext)
                if writer.transport.get_write_buffer_size() > 65536:
                    await writer.drain()
            except Exception as exc:
                log.debug("TCPIntermediateO.send error: %s %s", type(exc).__name__, exc)
                raise OSError(exc) from exc

    async def recv(self, length: int = 0) -> Optional[bytes]:
        async with self._recv_lock:
            raw_hdr = await super().recv(4)
            if raw_hdr is None:
                return None

            dec_hdr      = aes.ctr256_decrypt(raw_hdr, *self.decrypt)
            payload_size = _STRUCT_I.unpack_from(dec_hdr)[0]

            if payload_size < MIN_PACKET_SIZE or payload_size > MAX_PACKET_SIZE:
                log.warning(
                    "TCPIntermediateO: invalid payload size %d — discarding frame",
                    payload_size,
                )
                return None

            raw_body = await super().recv(payload_size)
            if raw_body is None:
                return None

            data = aes.ctr256_decrypt(raw_body, *self.decrypt)

            constructor = struct.unpack_from("<I", data, 0)[0] if len(data) >= 4 else 0
            log.debug(
                "TCPIntermediateO recv: payload=%d bytes  constructor=0x%08x  head16=%s",
                len(data),
                constructor,
                data[:16].hex(),
            )
            return data
