
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PublicForwards(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.stats.PublicForwards`.

    Details:
        - Layer: ``224``
        - ID: ``93037E20``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        forwards (List of :obj:`PublicForward <pyrogram.raw.base.PublicForward>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        next_offset (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stats.GetMessagePublicForwards
            stats.GetStoryPublicForwards
    """

    __slots__: List[str] = ["count", "forwards", "chats", "users", "next_offset"]

    ID = 0x93037e20
    QUALNAME = "types.stats.PublicForwards"

    def __init__(self, *, count: int, forwards: List["raw.base.PublicForward"], chats: List["raw.base.Chat"], users: List["raw.base.User"], next_offset: Optional[str] = None) -> None:
        self.count = count
        self.forwards = forwards
        self.chats = chats
        self.users = users
        self.next_offset = next_offset

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PublicForwards":
        
        flags = Int.read(b)
        
        count = Int.read(b)
        
        forwards = TLObject.read(b)
        
        next_offset = String.read(b) if flags & (1 << 0) else None
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return PublicForwards(count=count, forwards=forwards, chats=chats, users=users, next_offset=next_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.next_offset is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.count))
        
        b.write(Vector(self.forwards))
        
        if self.next_offset is not None:
            b.write(String(self.next_offset))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
