
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EditChatCreator(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``F743B857``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        password (:obj:`InputCheckPasswordSRP <pyrogram.raw.base.InputCheckPasswordSRP>`):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "user_id", "password"]

    ID = 0xf743b857
    QUALNAME = "functions.messages.EditChatCreator"

    def __init__(self, *, peer: "raw.base.InputPeer", user_id: "raw.base.InputUser", password: "raw.base.InputCheckPasswordSRP") -> None:
        self.peer = peer
        self.user_id = user_id
        self.password = password

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditChatCreator":
        
        peer = TLObject.read(b)
        
        user_id = TLObject.read(b)
        
        password = TLObject.read(b)
        
        return EditChatCreator(peer=peer, user_id=user_id, password=password)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(self.user_id.write())
        
        b.write(self.password.write())
        
        return b.getvalue()
