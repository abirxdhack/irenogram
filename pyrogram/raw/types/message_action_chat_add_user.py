
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageActionChatAddUser(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``15CEFD00``

    Parameters:
        users (List of ``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["users"]

    ID = 0x15cefd00
    QUALNAME = "types.MessageActionChatAddUser"

    def __init__(self, *, users: List[int]) -> None:
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionChatAddUser":
        
        users = TLObject.read(b, Long)
        
        return MessageActionChatAddUser(users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.users, Long))
        
        return b.getvalue()
