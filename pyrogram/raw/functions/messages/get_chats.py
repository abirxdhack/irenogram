
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetChats(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``49E9528F``

    Parameters:
        id (List of ``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`messages.Chats <pyrogram.raw.base.messages.Chats>`
    """

    __slots__: List[str] = ["id"]

    ID = 0x49e9528f
    QUALNAME = "functions.messages.GetChats"

    def __init__(self, *, id: List[int]) -> None:
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetChats":
        
        id = TLObject.read(b, Long)
        
        return GetChats(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.id, Long))
        
        return b.getvalue()
