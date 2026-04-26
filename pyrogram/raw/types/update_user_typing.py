
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateUserTyping(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``2A17BF5C``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        action (:obj:`SendMessageAction <pyrogram.raw.base.SendMessageAction>`):
            N/A

        top_msg_id (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["user_id", "action", "top_msg_id"]

    ID = 0x2a17bf5c
    QUALNAME = "types.UpdateUserTyping"

    def __init__(self, *, user_id: int, action: "raw.base.SendMessageAction", top_msg_id: Optional[int] = None) -> None:
        self.user_id = user_id
        self.action = action
        self.top_msg_id = top_msg_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateUserTyping":
        
        flags = Int.read(b)
        
        user_id = Long.read(b)
        
        top_msg_id = Int.read(b) if flags & (1 << 0) else None
        action = TLObject.read(b)
        
        return UpdateUserTyping(user_id=user_id, action=action, top_msg_id=top_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.top_msg_id is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.user_id))
        
        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))
        
        b.write(self.action.write())
        
        return b.getvalue()
