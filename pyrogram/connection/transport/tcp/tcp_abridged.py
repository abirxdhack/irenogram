
import logging
import struct
from typing import Optional, Tuple

from .tcp import TCP, Proxy

log = logging.getLogger(__name__)

MIN_PACKET_SIZE = 4

_SINGLE_BYTE_HEADERS = [bytes([i]) for i in range(128)]
_EXT_HEADER = b"\x7f"

class TCPAbridged(TCP):
    """
    MTProto Abridged transport (tag 0xEF).

    Frame format (outgoing / incoming):
      - Payload length in 4-byte words:
          1 byte  if length-in-words <= 126
          4 bytes (0x7F + 3-byte LE) if length-in-words > 126
      - Followed by the raw payload bytes.

    Atomicity guarantee: the entire two-step read (length header + body) is
    held under _recv_lock so that no other coroutine can consume bytes that
    belong to the current frame.
    """

    def __init__(self, ipv6: bool, proxy: Proxy) -> None:
        super().__init__(ipv6, proxy)

    async def connect(self, address: Tuple[str, int]) -> None:
        await super().connect(address)
        await super().send(b"\xef")

    async def send(self, data: bytes, *args) -> None:
        length_in_words = len(data) >> 2  

        if length_in_words <= 126:
            header = _SINGLE_BYTE_HEADERS[length_in_words]
        else:
            header = _EXT_HEADER + struct.pack("<I", length_in_words)[:3]

        await super().send(header + data)

    async def recv(self, length: int = 0) -> Optional[bytes]:
        async with self._recv_lock:
            header = await super().recv(1)
            if header is None:
                return None

            if header == _EXT_HEADER:
                ext = await super().recv(3)
                if ext is None:
                    return None
                length_in_words = struct.unpack("<I", ext + b"\x00")[0]
            else:
                length_in_words = header[0]

            payload_size = length_in_words << 2  

            if payload_size < MIN_PACKET_SIZE:
                log.warning(
                    "TCPAbridged: implausible payload size %d bytes — discarding frame",
                    payload_size,
                )
                return None

            data = await super().recv(payload_size)
            if data is None:
                return None

            constructor = struct.unpack_from("<I", data, 0)[0] if len(data) >= 4 else 0
            log.debug(
                "TCPAbridged recv: payload=%d bytes  constructor=0x%08x  head16=%s",
                len(data),
                constructor,
                data[:16].hex(),
            )
            return data
