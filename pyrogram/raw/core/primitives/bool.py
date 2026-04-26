
import struct
from io import BytesIO
from typing import Any

from ..tl_object import TLObject

_BOOL_FALSE_BYTES = struct.pack("<I", 0xBC799737)
_BOOL_TRUE_BYTES  = struct.pack("<I", 0x997275B5)
_BOOL_TRUE_ID     = 0x997275B5

_STRUCT_I = struct.Struct("<I")

class BoolFalse(bytes, TLObject):
    ID    = 0xBC799737
    value = False

    @classmethod
    def read(cls, *args: Any) -> bool:
        return cls.value

    def __new__(cls) -> bytes:
        return _BOOL_FALSE_BYTES

class BoolTrue(BoolFalse):
    ID    = 0x997275B5
    value = True

    def __new__(cls) -> bytes:
        return _BOOL_TRUE_BYTES

class Bool(bytes, TLObject):
    @classmethod
    def read(cls, data: BytesIO, *args: Any) -> bool:
        return _STRUCT_I.unpack(data.read(4))[0] == _BOOL_TRUE_ID

    def __new__(cls, value: bool) -> bytes:
        return _BOOL_TRUE_BYTES if value else _BOOL_FALSE_BYTES
