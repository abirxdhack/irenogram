
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class File(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.upload.File`.

    Details:
        - Layer: ``224``
        - ID: ``96A18D5``

    Parameters:
        type (:obj:`storage.FileType <pyrogram.raw.base.storage.FileType>`):
            N/A

        mtime (``int`` ``32-bit``):
            N/A

        bytes (``bytes``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            upload.GetFile
    """

    __slots__: List[str] = ["type", "mtime", "bytes"]

    ID = 0x96a18d5
    QUALNAME = "types.upload.File"

    def __init__(self, *, type: "raw.base.storage.FileType", mtime: int, bytes: bytes) -> None:
        self.type = type
        self.mtime = mtime
        self.bytes = bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "File":
        
        type = TLObject.read(b)
        
        mtime = Int.read(b)
        
        bytes = Bytes.read(b)
        
        return File(type=type, mtime=mtime, bytes=bytes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.type.write())
        
        b.write(Int(self.mtime))
        
        b.write(Bytes(self.bytes))
        
        return b.getvalue()
