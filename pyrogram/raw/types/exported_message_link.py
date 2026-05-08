
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ExportedMessageLink(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ExportedMessageLink`.

    Details:
        - Layer: ``224``
        - ID: ``5DAB1AF4``

    Parameters:
        link (``str``):
            N/A

        html (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            channels.ExportMessageLink
    """

    __slots__: List[str] = ["link", "html"]

    ID = 0x5dab1af4
    QUALNAME = "types.ExportedMessageLink"

    def __init__(self, *, link: str, html: str) -> None:
        self.link = link
        self.html = html

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedMessageLink":
        
        link = String.read(b)
        
        html = String.read(b)
        
        return ExportedMessageLink(link=link, html=html)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.link))
        
        b.write(String(self.html))
        
        return b.getvalue()
