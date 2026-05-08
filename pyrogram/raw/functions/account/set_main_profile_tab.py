
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SetMainProfileTab(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``5DEE78B0``

    Parameters:
        tab (:obj:`ProfileTab <pyrogram.raw.base.ProfileTab>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["tab"]

    ID = 0x5dee78b0
    QUALNAME = "functions.account.SetMainProfileTab"

    def __init__(self, *, tab: "raw.base.ProfileTab") -> None:
        self.tab = tab

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetMainProfileTab":
        
        tab = TLObject.read(b)
        
        return SetMainProfileTab(tab=tab)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.tab.write())
        
        return b.getvalue()
