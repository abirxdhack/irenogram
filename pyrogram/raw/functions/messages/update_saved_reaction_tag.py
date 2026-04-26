
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateSavedReactionTag(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``60297DEC``

    Parameters:
        reaction (:obj:`Reaction <pyrogram.raw.base.Reaction>`):
            N/A

        title (``str``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["reaction", "title"]

    ID = 0x60297dec
    QUALNAME = "functions.messages.UpdateSavedReactionTag"

    def __init__(self, *, reaction: "raw.base.Reaction", title: Optional[str] = None) -> None:
        self.reaction = reaction
        self.title = title

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateSavedReactionTag":
        
        flags = Int.read(b)
        
        reaction = TLObject.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        return UpdateSavedReactionTag(reaction=reaction, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.title is not None else 0
        b.write(Int(flags))
        
        b.write(self.reaction.write())
        
        if self.title is not None:
            b.write(String(self.title))
        
        return b.getvalue()
