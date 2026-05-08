
import logging
import struct
from typing import Optional, Tuple

from .tcp import TCP, Proxy

log = logging.getLogger(__name__)

MIN_PACKET_SIZE = 4
MAX_PACKET_SIZE = 16 * 1024 * 1024

_STRUCT_I = struct.Struct("<i")

class TCPIntermediate(TCP):
    """
    MTProto Intermediate transport (tag 0xEEEEEEEE).

    Frame format:
      4 bytes LE  — payload length in bytes
      N bytes     — raw payload

    Atomicity guarantee: the length header + body are read inside a single
    _recv_lock acquisition so no other coroutine can interleave reads.
    """

    def __init__(self, ipv6: bool, proxy: Proxy) -> None:
        super().__init__(ipv6, proxy)

    async def connect(self, address: Tuple[str, int]) -> None:
        await super().connect(address)
        await super().send(b"\xee" * 4)

    async def send(self, data: bytes, *args) -> None:
        await super().send(_STRUCT_I.pack(len(data)) + data)

    async def recv(self, length: int = 0) -> Optional[bytes]:
        async with self._recv_lock:
            hdr = await super().recv(4)
            if hdr is None:
                return None

            payload_size = _STRUCT_I.unpack_from(hdr)[0]

            if payload_size < MIN_PACKET_SIZE or payload_size > MAX_PACKET_SIZE:
                log.warning(
                    "TCPIntermediate: invalid payload size %d — discarding frame",
                    payload_size,
                )
                return None

            data = await super().recv(payload_size)
            if data is None:
                return None

            constructor = struct.unpack_from("<I", data, 0)[0] if len(data) >= 4 else 0
            log.debug(
                "TCPIntermediate recv: payload=%d bytes  constructor=0x%08x  head16=%s",
                len(data),
                constructor,
                data[:16].hex(),
            )
            return data
