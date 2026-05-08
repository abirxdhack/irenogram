
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PollAnswer(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PollAnswer`.

    Details:
        - Layer: ``224``
        - ID: ``4B7D786A``

    Parameters:
        text (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`):
            N/A

        option (``bytes``):
            N/A

        media (:obj:`MessageMedia <pyrogram.raw.base.MessageMedia>`, *optional*):
            N/A

        added_by (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

        date (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["text", "option", "media", "added_by", "date"]

    ID = 0x4b7d786a
    QUALNAME = "types.PollAnswer"

    def __init__(self, *, text: "raw.base.TextWithEntities", option: bytes, media: "raw.base.MessageMedia" = None, added_by: "raw.base.Peer" = None, date: Optional[int] = None) -> None:
        self.text = text
        self.option = option
        self.media = media
        self.added_by = added_by
        self.date = date

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PollAnswer":
        
        flags = Int.read(b)
        
        text = TLObject.read(b)
        
        option = Bytes.read(b)
        
        media = TLObject.read(b) if flags & (1 << 0) else None
        
        added_by = TLObject.read(b) if flags & (1 << 1) else None
        
        date = Int.read(b) if flags & (1 << 1) else None
        return PollAnswer(text=text, option=option, media=media, added_by=added_by, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.media is not None else 0
        flags |= (1 << 1) if self.added_by is not None else 0
        flags |= (1 << 1) if self.date is not None else 0
        b.write(Int(flags))
        
        b.write(self.text.write())
        
        b.write(Bytes(self.option))
        
        if self.media is not None:
            b.write(self.media.write())
        
        if self.added_by is not None:
            b.write(self.added_by.write())
        
        if self.date is not None:
            b.write(Int(self.date))
        
        return b.getvalue()
