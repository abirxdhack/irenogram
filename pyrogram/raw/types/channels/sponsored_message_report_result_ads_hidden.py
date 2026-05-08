
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SponsoredMessageReportResultAdsHidden(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.channels.SponsoredMessageReportResult`.

    Details:
        - Layer: ``224``
        - ID: ``3E3BCF2F``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.ReportSponsoredMessage
    """

    __slots__: List[str] = []

    ID = 0x3e3bcf2f
    QUALNAME = "types.channels.SponsoredMessageReportResultAdsHidden"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SponsoredMessageReportResultAdsHidden":
        
        return SponsoredMessageReportResultAdsHidden()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
