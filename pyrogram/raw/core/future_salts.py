
import struct
from io import BytesIO
from typing import Any, List

from .future_salt import FutureSalt
from .primitives.int import Int, Long
from .tl_object import TLObject

_ID_BYTES   = struct.pack("<I", 0xAE500895)
_STRUCT_QI  = struct.Struct("<qi")

class FutureSalts(TLObject):
    ID = 0xAE500895

    __slots__ = ["req_msg_id", "now", "salts"]

    QUALNAME = "FutureSalts"

    def __init__(self, req_msg_id: int, now: int, salts: List[FutureSalt]):
        self.req_msg_id = req_msg_id
        self.now        = now
        self.salts      = salts

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "FutureSalts":
        req_msg_id, now = _STRUCT_QI.unpack(data.read(12))
        count  = struct.unpack_from("<i", data.read(4))[0]
        salts  = [FutureSalt.read(data) for _ in range(count)]
        return FutureSalts(req_msg_id, now, salts)

    def write(self, *args: Any) -> bytes:
        salts   = self.salts
        count   = len(salts)
        parts   = [_ID_BYTES, _STRUCT_QI.pack(self.req_msg_id, self.now), struct.pack("<i", count)]
        parts.extend(s.write() for s in salts)
        return b"".join(parts)
