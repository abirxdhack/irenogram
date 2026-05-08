
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UnregisterDevice(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``6A0D3206``

    Parameters:
        token_type (``int`` ``32-bit``):
            N/A

        token (``str``):
            N/A

        other_uids (List of ``int`` ``64-bit``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["token_type", "token", "other_uids"]

    ID = 0x6a0d3206
    QUALNAME = "functions.account.UnregisterDevice"

    def __init__(self, *, token_type: int, token: str, other_uids: List[int]) -> None:
        self.token_type = token_type
        self.token = token
        self.other_uids = other_uids

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UnregisterDevice":
        
        token_type = Int.read(b)
        
        token = String.read(b)
        
        other_uids = TLObject.read(b, Long)
        
        return UnregisterDevice(token_type=token_type, token=token, other_uids=other_uids)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.token_type))
        
        b.write(String(self.token))
        
        b.write(Vector(self.other_uids, Long))
        
        return b.getvalue()
