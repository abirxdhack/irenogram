
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PaymentSavedCredentialsCard(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PaymentSavedCredentials`.

    Details:
        - Layer: ``224``
        - ID: ``CDC27A1F``

    Parameters:
        id (``str``):
            N/A

        title (``str``):
            N/A

    """

    __slots__: List[str] = ["id", "title"]

    ID = 0xcdc27a1f
    QUALNAME = "types.PaymentSavedCredentialsCard"

    def __init__(self, *, id: str, title: str) -> None:
        self.id = id
        self.title = title

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PaymentSavedCredentialsCard":
        
        id = String.read(b)
        
        title = String.read(b)
        
        return PaymentSavedCredentialsCard(id=id, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.id))
        
        b.write(String(self.title))
        
        return b.getvalue()
