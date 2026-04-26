
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageViews(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageViews`.

    Details:
        - Layer: ``224``
        - ID: ``455B853D``

    Parameters:
        views (``int`` ``32-bit``, *optional*):
            N/A

        forwards (``int`` ``32-bit``, *optional*):
            N/A

        replies (:obj:`MessageReplies <pyrogram.raw.base.MessageReplies>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["views", "forwards", "replies"]

    ID = 0x455b853d
    QUALNAME = "types.MessageViews"

    def __init__(self, *, views: Optional[int] = None, forwards: Optional[int] = None, replies: "raw.base.MessageReplies" = None) -> None:
        self.views = views
        self.forwards = forwards
        self.replies = replies

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageViews":
        
        flags = Int.read(b)
        
        views = Int.read(b) if flags & (1 << 0) else None
        forwards = Int.read(b) if flags & (1 << 1) else None
        replies = TLObject.read(b) if flags & (1 << 2) else None
        
        return MessageViews(views=views, forwards=forwards, replies=replies)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.views is not None else 0
        flags |= (1 << 1) if self.forwards is not None else 0
        flags |= (1 << 2) if self.replies is not None else 0
        b.write(Int(flags))
        
        if self.views is not None:
            b.write(Int(self.views))
        
        if self.forwards is not None:
            b.write(Int(self.forwards))
        
        if self.replies is not None:
            b.write(self.replies.write())
        
        return b.getvalue()
