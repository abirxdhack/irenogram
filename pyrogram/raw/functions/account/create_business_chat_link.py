
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class CreateBusinessChatLink(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``8851E68E``

    Parameters:
        link (:obj:`InputBusinessChatLink <pyrogram.raw.base.InputBusinessChatLink>`):
            N/A

    Returns:
        :obj:`BusinessChatLink <pyrogram.raw.base.BusinessChatLink>`
    """

    __slots__: List[str] = ["link"]

    ID = 0x8851e68e
    QUALNAME = "functions.account.CreateBusinessChatLink"

    def __init__(self, *, link: "raw.base.InputBusinessChatLink") -> None:
        self.link = link

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateBusinessChatLink":
        
        link = TLObject.read(b)
        
        return CreateBusinessChatLink(link=link)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.link.write())
        
        return b.getvalue()
