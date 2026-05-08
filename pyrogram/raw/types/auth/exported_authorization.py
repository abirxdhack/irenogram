
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ExportedAuthorization(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.auth.ExportedAuthorization`.

    Details:
        - Layer: ``224``
        - ID: ``B434E2B8``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        bytes (``bytes``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.ExportAuthorization
    """

    __slots__: List[str] = ["id", "bytes"]

    ID = 0xb434e2b8
    QUALNAME = "types.auth.ExportedAuthorization"

    def __init__(self, *, id: int, bytes: bytes) -> None:
        self.id = id
        self.bytes = bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedAuthorization":
        
        id = Long.read(b)
        
        bytes = Bytes.read(b)
        
        return ExportedAuthorization(id=id, bytes=bytes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.id))
        
        b.write(Bytes(self.bytes))
        
        return b.getvalue()
