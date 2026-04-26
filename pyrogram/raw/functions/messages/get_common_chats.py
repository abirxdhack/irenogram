
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetCommonChats(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``E40CA104``

    Parameters:
        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        max_id (``int`` ``64-bit``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`messages.Chats <pyrogram.raw.base.messages.Chats>`
    """

    __slots__: List[str] = ["user_id", "max_id", "limit"]

    ID = 0xe40ca104
    QUALNAME = "functions.messages.GetCommonChats"

    def __init__(self, *, user_id: "raw.base.InputUser", max_id: int, limit: int) -> None:
        self.user_id = user_id
        self.max_id = max_id
        self.limit = limit

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetCommonChats":
        
        user_id = TLObject.read(b)
        
        max_id = Long.read(b)
        
        limit = Int.read(b)
        
        return GetCommonChats(user_id=user_id, max_id=max_id, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.user_id.write())
        
        b.write(Long(self.max_id))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
