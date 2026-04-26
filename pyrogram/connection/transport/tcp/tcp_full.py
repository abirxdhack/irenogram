
import logging
import struct
from binascii import crc32
from typing import Optional, Tuple

from .tcp import TCP, Proxy

log = logging.getLogger(__name__)

MIN_PACKET_SIZE = 12
MAX_PACKET_SIZE = 16 * 1024 * 1024

_STRUCT_II  = struct.Struct("<II")
_STRUCT_I   = struct.Struct("<I")

class TCPFull(TCP):
    """
    MTProto Full transport.

    Frame format:
      4 bytes LE  — total frame length (including this field, seq_no, and CRC)
      4 bytes LE  — seq_no
      N bytes     — payload
      4 bytes LE  — CRC32 of all preceding bytes

    Atomicity guarantee: length header + body + CRC are all read under a
    single _recv_lock acquisition.  CRC is validated before returning data.
    """

    def __init__(self, ipv6: bool, proxy: Proxy) -> None:
        super().__init__(ipv6, proxy)
        self.seq_no: int = 0

    async def connect(self, address: Tuple[str, int]) -> None:
        await super().connect(address)
        self.seq_no = 0

    async def send(self, data: bytes, *args) -> None:
        frame  = _STRUCT_II.pack(len(data) + 12, self.seq_no) + data
        frame += _STRUCT_I.pack(crc32(frame) & 0xFFFFFFFF)
        self.seq_no += 1
        await super().send(frame)

    async def recv(self, length: int = 0) -> Optional[bytes]:
        async with self._recv_lock:
            hdr = await super().recv(4)
            if hdr is None:
                return None

            total_length = _STRUCT_I.unpack_from(hdr)[0]

            if total_length < MIN_PACKET_SIZE or total_length > MAX_PACKET_SIZE:
                log.warning(
                    "TCPFull: invalid frame length %d — discarding frame",
                    total_length,
                )
                return None

            rest = await super().recv(total_length - 4)
            if rest is None:
                return None

            frame    = hdr + rest
            checksum = _STRUCT_I.unpack_from(frame, len(frame) - 4)[0]
            body     = frame[:-4]

            if (crc32(body) & 0xFFFFFFFF) != checksum:
                log.warning("TCPFull: CRC mismatch — discarding frame")
                return None

            data = body[8:]

            constructor = struct.unpack_from("<I", data, 0)[0] if len(data) >= 4 else 0
            log.debug(
                "TCPFull recv: payload=%d bytes  constructor=0x%08x  head16=%s",
                len(data),
                constructor,
                data[:16].hex(),
            )
            return data
