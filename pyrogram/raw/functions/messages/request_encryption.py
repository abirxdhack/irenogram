
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class RequestEncryption(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``F64DAF43``

    Parameters:
        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        random_id (``int`` ``32-bit``):
            N/A

        g_a (``bytes``):
            N/A

    Returns:
        :obj:`EncryptedChat <pyrogram.raw.base.EncryptedChat>`
    """

    __slots__: List[str] = ["user_id", "random_id", "g_a"]

    ID = 0xf64daf43
    QUALNAME = "functions.messages.RequestEncryption"

    def __init__(self, *, user_id: "raw.base.InputUser", random_id: int, g_a: bytes) -> None:
        self.user_id = user_id
        self.random_id = random_id
        self.g_a = g_a

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestEncryption":
        
        user_id = TLObject.read(b)
        
        random_id = Int.read(b)
        
        g_a = Bytes.read(b)
        
        return RequestEncryption(user_id=user_id, random_id=random_id, g_a=g_a)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.user_id.write())
        
        b.write(Int(self.random_id))
        
        b.write(Bytes(self.g_a))
        
        return b.getvalue()
