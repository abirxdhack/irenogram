
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputStickerSetThumb(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputFileLocation`.

    Details:
        - Layer: ``224``
        - ID: ``9D84F3DB``

    Parameters:
        stickerset (:obj:`InputStickerSet <pyrogram.raw.base.InputStickerSet>`):
            N/A

        thumb_version (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["stickerset", "thumb_version"]

    ID = 0x9d84f3db
    QUALNAME = "types.InputStickerSetThumb"

    def __init__(self, *, stickerset: "raw.base.InputStickerSet", thumb_version: int) -> None:
        self.stickerset = stickerset
        self.thumb_version = thumb_version

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStickerSetThumb":
        
        stickerset = TLObject.read(b)
        
        thumb_version = Int.read(b)
        
        return InputStickerSetThumb(stickerset=stickerset, thumb_version=thumb_version)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.stickerset.write())
        
        b.write(Int(self.thumb_version))
        
        return b.getvalue()
