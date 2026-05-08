
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputPaymentCredentialsApplePay(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputPaymentCredentials`.

    Details:
        - Layer: ``224``
        - ID: ``AA1C39F``

    Parameters:
        payment_data (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`):
            N/A

    """

    __slots__: List[str] = ["payment_data"]

    ID = 0xaa1c39f
    QUALNAME = "types.InputPaymentCredentialsApplePay"

    def __init__(self, *, payment_data: "raw.base.DataJSON") -> None:
        self.payment_data = payment_data

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPaymentCredentialsApplePay":
        
        payment_data = TLObject.read(b)
        
        return InputPaymentCredentialsApplePay(payment_data=payment_data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.payment_data.write())
        
        return b.getvalue()
