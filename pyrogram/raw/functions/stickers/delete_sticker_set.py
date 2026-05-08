
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DeleteStickerSet(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``87704394``

    Parameters:
        stickerset (:obj:`InputStickerSet <pyrogram.raw.base.InputStickerSet>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["stickerset"]

    ID = 0x87704394
    QUALNAME = "functions.stickers.DeleteStickerSet"

    def __init__(self, *, stickerset: "raw.base.InputStickerSet") -> None:
        self.stickerset = stickerset

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteStickerSet":
        
        stickerset = TLObject.read(b)
        
        return DeleteStickerSet(stickerset=stickerset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.stickerset.write())
        
        return b.getvalue()
