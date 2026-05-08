
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ResolveBusinessChatLink(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``5492E5EE``

    Parameters:
        slug (``str``):
            N/A

    Returns:
        :obj:`account.ResolvedBusinessChatLinks <pyrogram.raw.base.account.ResolvedBusinessChatLinks>`
    """

    __slots__: List[str] = ["slug"]

    ID = 0x5492e5ee
    QUALNAME = "functions.account.ResolveBusinessChatLink"

    def __init__(self, *, slug: str) -> None:
        self.slug = slug

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResolveBusinessChatLink":
        
        slug = String.read(b)
        
        return ResolveBusinessChatLink(slug=slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.slug))
        
        return b.getvalue()
