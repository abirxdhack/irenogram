
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DeleteBusinessChatLink(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``60073674``

    Parameters:
        slug (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["slug"]

    ID = 0x60073674
    QUALNAME = "functions.account.DeleteBusinessChatLink"

    def __init__(self, *, slug: str) -> None:
        self.slug = slug

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteBusinessChatLink":
        
        slug = String.read(b)
        
        return DeleteBusinessChatLink(slug=slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.slug))
        
        return b.getvalue()
