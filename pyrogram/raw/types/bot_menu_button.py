
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class BotMenuButton(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BotMenuButton`.

    Details:
        - Layer: ``224``
        - ID: ``C7B57CE6``

    Parameters:
        text (``str``):
            N/A

        url (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.GetBotMenuButton
    """

    __slots__: List[str] = ["text", "url"]

    ID = 0xc7b57ce6
    QUALNAME = "types.BotMenuButton"

    def __init__(self, *, text: str, url: str) -> None:
        self.text = text
        self.url = url

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotMenuButton":
        
        text = String.read(b)
        
        url = String.read(b)
        
        return BotMenuButton(text=text, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.text))
        
        b.write(String(self.url))
        
        return b.getvalue()
