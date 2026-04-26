
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ExportedStoryLink(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ExportedStoryLink`.

    Details:
        - Layer: ``224``
        - ID: ``3FC9053B``

    Parameters:
        link (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.ExportStoryLink
    """

    __slots__: List[str] = ["link"]

    ID = 0x3fc9053b
    QUALNAME = "types.ExportedStoryLink"

    def __init__(self, *, link: str) -> None:
        self.link = link

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedStoryLink":
        
        link = String.read(b)
        
        return ExportedStoryLink(link=link)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.link))
        
        return b.getvalue()
