
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ExportedGroupCallInvite(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.phone.ExportedGroupCallInvite`.

    Details:
        - Layer: ``224``
        - ID: ``204BD158``

    Parameters:
        link (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            phone.ExportGroupCallInvite
    """

    __slots__: List[str] = ["link"]

    ID = 0x204bd158
    QUALNAME = "types.phone.ExportedGroupCallInvite"

    def __init__(self, *, link: str) -> None:
        self.link = link

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedGroupCallInvite":
        
        link = String.read(b)
        
        return ExportedGroupCallInvite(link=link)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.link))
        
        return b.getvalue()
