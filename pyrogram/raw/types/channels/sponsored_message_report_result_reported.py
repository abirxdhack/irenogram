
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SponsoredMessageReportResultReported(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.channels.SponsoredMessageReportResult`.

    Details:
        - Layer: ``224``
        - ID: ``AD798849``

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

    ID = 0xad798849
    QUALNAME = "types.channels.SponsoredMessageReportResultReported"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SponsoredMessageReportResultReported":
        
        return SponsoredMessageReportResultReported()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
