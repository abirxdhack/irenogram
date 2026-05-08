
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChatReactionsSome(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChatReactions`.

    Details:
        - Layer: ``224``
        - ID: ``661D4037``

    Parameters:
        reactions (List of :obj:`Reaction <pyrogram.raw.base.Reaction>`):
            N/A

    """

    __slots__: List[str] = ["reactions"]

    ID = 0x661d4037
    QUALNAME = "types.ChatReactionsSome"

    def __init__(self, *, reactions: List["raw.base.Reaction"]) -> None:
        self.reactions = reactions

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatReactionsSome":
        
        reactions = TLObject.read(b)
        
        return ChatReactionsSome(reactions=reactions)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.reactions))
        
        return b.getvalue()
