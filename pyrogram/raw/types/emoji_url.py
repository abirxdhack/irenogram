
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EmojiURL(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.EmojiURL`.

    Details:
        - Layer: ``224``
        - ID: ``A575739D``

    Parameters:
        url (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetEmojiURL
    """

    __slots__: List[str] = ["url"]

    ID = 0xa575739d
    QUALNAME = "types.EmojiURL"

    def __init__(self, *, url: str) -> None:
        self.url = url

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiURL":
        
        url = String.read(b)
        
        return EmojiURL(url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.url))
        
        return b.getvalue()
