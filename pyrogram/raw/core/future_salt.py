
import struct
from io import BytesIO
from typing import Any

from .primitives.int import Int, Long
from .tl_object import TLObject

_STRUCT_IIQ = struct.Struct("<iiq")

class FutureSalt(TLObject):
    ID = 0x0949D9DC

    __slots__ = ["valid_since", "valid_until", "salt"]

    QUALNAME = "FutureSalt"

    def __init__(self, valid_since: int, valid_until: int, salt: int):
        self.valid_since = valid_since
        self.valid_until = valid_until
        self.salt        = salt

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "FutureSalt":
        vs, vu, salt = _STRUCT_IIQ.unpack(data.read(16))
        return FutureSalt(vs, vu, salt)

    def write(self, *args: Any) -> bytes:
        return _STRUCT_IIQ.pack(self.valid_since, self.valid_until, self.salt)
