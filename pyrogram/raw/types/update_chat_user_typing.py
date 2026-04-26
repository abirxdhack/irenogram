
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateChatUserTyping(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``83487AF0``

    Parameters:
        chat_id (``int`` ``64-bit``):
            N/A

        from_id (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        action (:obj:`SendMessageAction <pyrogram.raw.base.SendMessageAction>`):
            N/A

    """

    __slots__: List[str] = ["chat_id", "from_id", "action"]

    ID = 0x83487af0
    QUALNAME = "types.UpdateChatUserTyping"

    def __init__(self, *, chat_id: int, from_id: "raw.base.Peer", action: "raw.base.SendMessageAction") -> None:
        self.chat_id = chat_id
        self.from_id = from_id
        self.action = action

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChatUserTyping":
        
        chat_id = Long.read(b)
        
        from_id = TLObject.read(b)
        
        action = TLObject.read(b)
        
        return UpdateChatUserTyping(chat_id=chat_id, from_id=from_id, action=action)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.chat_id))
        
        b.write(self.from_id.write())
        
        b.write(self.action.write())
        
        return b.getvalue()
