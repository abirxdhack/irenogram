
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class CheckChatlistInvite(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``41C10FFF``

    Parameters:
        slug (``str``):
            N/A

    Returns:
        :obj:`chatlists.ChatlistInvite <pyrogram.raw.base.chatlists.ChatlistInvite>`
    """

    __slots__: List[str] = ["slug"]

    ID = 0x41c10fff
    QUALNAME = "functions.chatlists.CheckChatlistInvite"

    def __init__(self, *, slug: str) -> None:
        self.slug = slug

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckChatlistInvite":
        
        slug = String.read(b)
        
        return CheckChatlistInvite(slug=slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.slug))
        
        return b.getvalue()
