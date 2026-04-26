
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PaymentCharge(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PaymentCharge`.

    Details:
        - Layer: ``224``
        - ID: ``EA02C27E``

    Parameters:
        id (``str``):
            N/A

        provider_charge_id (``str``):
            N/A

    """

    __slots__: List[str] = ["id", "provider_charge_id"]

    ID = 0xea02c27e
    QUALNAME = "types.PaymentCharge"

    def __init__(self, *, id: str, provider_charge_id: str) -> None:
        self.id = id
        self.provider_charge_id = provider_charge_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PaymentCharge":
        
        id = String.read(b)
        
        provider_charge_id = String.read(b)
        
        return PaymentCharge(id=id, provider_charge_id=provider_charge_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.id))
        
        b.write(String(self.provider_charge_id))
        
        return b.getvalue()
