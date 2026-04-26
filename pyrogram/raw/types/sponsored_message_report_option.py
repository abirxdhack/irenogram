
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SponsoredMessageReportOption(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SponsoredMessageReportOption`.

    Details:
        - Layer: ``224``
        - ID: ``430D3150``

    Parameters:
        text (``str``):
            N/A

        option (``bytes``):
            N/A

    """

    __slots__: List[str] = ["text", "option"]

    ID = 0x430d3150
    QUALNAME = "types.SponsoredMessageReportOption"

    def __init__(self, *, text: str, option: bytes) -> None:
        self.text = text
        self.option = option

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SponsoredMessageReportOption":
        
        text = String.read(b)
        
        option = Bytes.read(b)
        
        return SponsoredMessageReportOption(text=text, option=option)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.text))
        
        b.write(Bytes(self.option))
        
        return b.getvalue()
