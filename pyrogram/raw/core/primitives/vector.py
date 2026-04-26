
import struct
from io import BytesIO
from typing import cast, Union, Any

from .bool import BoolFalse, BoolTrue, Bool
from .int import Int, Long
from ..list import List
from ..tl_object import TLObject

_BOOL_IDS = frozenset((BoolFalse.ID, BoolTrue.ID))
_STRUCT_I = struct.Struct("<i")
_STRUCT_I_ID = struct.Struct("<I")
_VECTOR_ID_BYTES = struct.pack("<I", 0x1CB5C415)

class Vector(bytes, TLObject):
    ID = 0x1CB5C415

    @staticmethod
    def read_bare(b: BytesIO, size: int) -> Union[int, Any]:
        if size == 4:
            raw = b.read(4)
            e   = _STRUCT_I_ID.unpack_from(raw)[0]
            b.seek(-4, 1)
            if e in _BOOL_IDS:
                return Bool.read(b)
            return _STRUCT_I.unpack_from(raw)[0]

        if size == 8:
            return Long.read(b)

        return TLObject.read(b)

    @classmethod
    def read(cls, data: BytesIO, t: Any = None, *args: Any) -> List:
        count = _STRUCT_I.unpack(data.read(4))[0]
        if count == 0:
            return List()
        left = len(data.read())
        size = left / count
        data.seek(-left, 1)

        return List(
            t.read(data) if t
            else Vector.read_bare(data, size)
            for _ in range(count)
        )

    def __new__(cls, value: list, t: Any = None) -> bytes:
        count = len(value)
        parts = [_VECTOR_ID_BYTES, struct.pack("<i", count)]
        if t is not None:
            parts.extend(cast(bytes, t(i)) for i in value)
        else:
            parts.extend(i.write() for i in value)
        return b"".join(parts)
