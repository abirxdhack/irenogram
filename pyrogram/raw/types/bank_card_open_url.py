
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class BankCardOpenUrl(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BankCardOpenUrl`.

    Details:
        - Layer: ``224``
        - ID: ``F568028A``

    Parameters:
        url (``str``):
            N/A

        name (``str``):
            N/A

    """

    __slots__: List[str] = ["url", "name"]

    ID = 0xf568028a
    QUALNAME = "types.BankCardOpenUrl"

    def __init__(self, *, url: str, name: str) -> None:
        self.url = url
        self.name = name

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BankCardOpenUrl":
        
        url = String.read(b)
        
        name = String.read(b)
        
        return BankCardOpenUrl(url=url, name=name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.url))
        
        b.write(String(self.name))
        
        return b.getvalue()
