
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SetStickerSetThumb(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``A76A5392``

    Parameters:
        stickerset (:obj:`InputStickerSet <pyrogram.raw.base.InputStickerSet>`):
            N/A

        thumb (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`, *optional*):
            N/A

        thumb_document_id (``int`` ``64-bit``, *optional*):
            N/A

    Returns:
        :obj:`messages.StickerSet <pyrogram.raw.base.messages.StickerSet>`
    """

    __slots__: List[str] = ["stickerset", "thumb", "thumb_document_id"]

    ID = 0xa76a5392
    QUALNAME = "functions.stickers.SetStickerSetThumb"

    def __init__(self, *, stickerset: "raw.base.InputStickerSet", thumb: "raw.base.InputDocument" = None, thumb_document_id: Optional[int] = None) -> None:
        self.stickerset = stickerset
        self.thumb = thumb
        self.thumb_document_id = thumb_document_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetStickerSetThumb":
        
        flags = Int.read(b)
        
        stickerset = TLObject.read(b)
        
        thumb = TLObject.read(b) if flags & (1 << 0) else None
        
        thumb_document_id = Long.read(b) if flags & (1 << 1) else None
        return SetStickerSetThumb(stickerset=stickerset, thumb=thumb, thumb_document_id=thumb_document_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.thumb is not None else 0
        flags |= (1 << 1) if self.thumb_document_id is not None else 0
        b.write(Int(flags))
        
        b.write(self.stickerset.write())
        
        if self.thumb is not None:
            b.write(self.thumb.write())
        
        if self.thumb_document_id is not None:
            b.write(Long(self.thumb_document_id))
        
        return b.getvalue()
