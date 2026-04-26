
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class AutoDownloadSettings(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.account.AutoDownloadSettings`.

    Details:
        - Layer: ``224``
        - ID: ``63CACF26``

    Parameters:
        low (:obj:`AutoDownloadSettings <pyrogram.raw.base.AutoDownloadSettings>`):
            N/A

        medium (:obj:`AutoDownloadSettings <pyrogram.raw.base.AutoDownloadSettings>`):
            N/A

        high (:obj:`AutoDownloadSettings <pyrogram.raw.base.AutoDownloadSettings>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetAutoDownloadSettings
    """

    __slots__: List[str] = ["low", "medium", "high"]

    ID = 0x63cacf26
    QUALNAME = "types.account.AutoDownloadSettings"

    def __init__(self, *, low: "raw.base.AutoDownloadSettings", medium: "raw.base.AutoDownloadSettings", high: "raw.base.AutoDownloadSettings") -> None:
        self.low = low
        self.medium = medium
        self.high = high

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AutoDownloadSettings":
        
        low = TLObject.read(b)
        
        medium = TLObject.read(b)
        
        high = TLObject.read(b)
        
        return AutoDownloadSettings(low=low, medium=medium, high=high)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.low.write())
        
        b.write(self.medium.write())
        
        b.write(self.high.write())
        
        return b.getvalue()
