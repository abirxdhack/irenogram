
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ImportChatInvite(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``6C50051C``

    Parameters:
        hash (``str``):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0x6c50051c
    QUALNAME = "functions.messages.ImportChatInvite"

    def __init__(self, *, hash: str) -> None:
        self.hash = hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ImportChatInvite":
        
        hash = String.read(b)
        
        return ImportChatInvite(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.hash))
        
        return b.getvalue()
