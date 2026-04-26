
from gzip import decompress
import zlib
from io import BytesIO
from typing import cast, Any

from .primitives.bytes import Bytes
from .primitives.int import Int
from .tl_object import TLObject

_GZIP_ID_BYTES = Int(0x3072CFA1, False)

class GzipPacked(TLObject):
    ID = 0x3072CFA1

    __slots__ = ["packed_data"]

    QUALNAME = "GzipPacked"

    def __init__(self, packed_data: TLObject):
        self.packed_data = packed_data

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GzipPacked":

        return cast(GzipPacked, TLObject.read(
            BytesIO(
                decompress(Bytes.read(data))
            )
        ))

    def write(self, *args: Any) -> bytes:

        compressed = zlib.compress(self.packed_data.write(), level=6, wbits=31)
        return _GZIP_ID_BYTES + Bytes(compressed)
