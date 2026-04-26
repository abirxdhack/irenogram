
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EditBusinessChatLink(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``8C3410AF``

    Parameters:
        slug (``str``):
            N/A

        link (:obj:`InputBusinessChatLink <pyrogram.raw.base.InputBusinessChatLink>`):
            N/A

    Returns:
        :obj:`BusinessChatLink <pyrogram.raw.base.BusinessChatLink>`
    """

    __slots__: List[str] = ["slug", "link"]

    ID = 0x8c3410af
    QUALNAME = "functions.account.EditBusinessChatLink"

    def __init__(self, *, slug: str, link: "raw.base.InputBusinessChatLink") -> None:
        self.slug = slug
        self.link = link

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditBusinessChatLink":
        
        slug = String.read(b)
        
        link = TLObject.read(b)
        
        return EditBusinessChatLink(slug=slug, link=link)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.slug))
        
        b.write(self.link.write())
        
        return b.getvalue()
