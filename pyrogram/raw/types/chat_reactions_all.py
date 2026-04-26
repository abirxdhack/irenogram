
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChatReactionsAll(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChatReactions`.

    Details:
        - Layer: ``224``
        - ID: ``52928BCA``

    Parameters:
        allow_custom (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["allow_custom"]

    ID = 0x52928bca
    QUALNAME = "types.ChatReactionsAll"

    def __init__(self, *, allow_custom: Optional[bool] = None) -> None:
        self.allow_custom = allow_custom

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatReactionsAll":
        
        flags = Int.read(b)
        
        allow_custom = True if flags & (1 << 0) else False
        return ChatReactionsAll(allow_custom=allow_custom)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.allow_custom else 0
        b.write(Int(flags))
        
        return b.getvalue()
