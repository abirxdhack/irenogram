
import struct
from io import BytesIO
from typing import Any

from ..tl_object import TLObject

_STRUCT_4S  = struct.Struct("<i")   
_STRUCT_4U  = struct.Struct("<I")   
_STRUCT_8S  = struct.Struct("<q")   
_STRUCT_8U  = struct.Struct("<Q")   
_STRUCT_16  = struct.Struct("<16s") 
_STRUCT_32  = struct.Struct("<32s") 

_INT_CACHE: dict = {}
for _v in range(-256, 4096):
    _INT_CACHE[_v] = _v.to_bytes(4, "little", signed=(_v < 0))

_LONG_CACHE: dict = {}
for _v in (0, 1, -1):
    _LONG_CACHE[_v] = _v.to_bytes(8, "little", signed=True)

class Int(bytes, TLObject):
    SIZE = 4

    @classmethod
    def read(cls, data: BytesIO, signed: bool = True, *args: Any) -> int:
        return _STRUCT_4S.unpack(data.read(4))[0] if signed else _STRUCT_4U.unpack(data.read(4))[0]

    def __new__(cls, value: int, signed: bool = True) -> bytes:
        if signed:
            cached = _INT_CACHE.get(value)
            if cached is not None:
                return cached
            return value.to_bytes(4, "little", signed=True)

        cached = _INT_CACHE.get(value)
        if cached is not None and value >= 0:
            return cached
        return value.to_bytes(4, "little", signed=False)

class Long(Int):
    SIZE = 8

    @classmethod
    def read(cls, data: BytesIO, signed: bool = True, *args: Any) -> int:
        return _STRUCT_8S.unpack(data.read(8))[0] if signed else _STRUCT_8U.unpack(data.read(8))[0]

    def __new__(cls, value: int, signed: bool = True) -> bytes:
        cached = _LONG_CACHE.get(value)
        if cached is not None:
            return cached
        return value.to_bytes(8, "little", signed=signed)

class Int128(Int):
    SIZE = 16

    @classmethod
    def read(cls, data: BytesIO, signed: bool = True, *args: Any) -> int:
        return int.from_bytes(data.read(16), "little", signed=signed)

    def __new__(cls, value: int, signed: bool = True) -> bytes:
        return value.to_bytes(16, "little", signed=signed)

class Int256(Int):
    SIZE = 32

    @classmethod
    def read(cls, data: BytesIO, signed: bool = True, *args: Any) -> int:
        return int.from_bytes(data.read(32), "little", signed=signed)

    def __new__(cls, value: int, signed: bool = True) -> bytes:
        return value.to_bytes(32, "little", signed=signed)
