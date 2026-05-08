
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class BankCardData(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.BankCardData`.

    Details:
        - Layer: ``224``
        - ID: ``3E24E573``

    Parameters:
        title (``str``):
            N/A

        open_urls (List of :obj:`BankCardOpenUrl <pyrogram.raw.base.BankCardOpenUrl>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetBankCardData
    """

    __slots__: List[str] = ["title", "open_urls"]

    ID = 0x3e24e573
    QUALNAME = "types.payments.BankCardData"

    def __init__(self, *, title: str, open_urls: List["raw.base.BankCardOpenUrl"]) -> None:
        self.title = title
        self.open_urls = open_urls

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BankCardData":
        
        title = String.read(b)
        
        open_urls = TLObject.read(b)
        
        return BankCardData(title=title, open_urls=open_urls)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.title))
        
        b.write(Vector(self.open_urls))
        
        return b.getvalue()
