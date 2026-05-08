
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ValidatedRequestedInfo(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.ValidatedRequestedInfo`.

    Details:
        - Layer: ``224``
        - ID: ``D1451883``

    Parameters:
        id (``str``, *optional*):
            N/A

        shipping_options (List of :obj:`ShippingOption <pyrogram.raw.base.ShippingOption>`, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.ValidateRequestedInfo
    """

    __slots__: List[str] = ["id", "shipping_options"]

    ID = 0xd1451883
    QUALNAME = "types.payments.ValidatedRequestedInfo"

    def __init__(self, *, id: Optional[str] = None, shipping_options: Optional[List["raw.base.ShippingOption"]] = None) -> None:
        self.id = id
        self.shipping_options = shipping_options

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ValidatedRequestedInfo":
        
        flags = Int.read(b)
        
        id = String.read(b) if flags & (1 << 0) else None
        shipping_options = TLObject.read(b) if flags & (1 << 1) else []
        
        return ValidatedRequestedInfo(id=id, shipping_options=shipping_options)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.id is not None else 0
        flags |= (1 << 1) if self.shipping_options else 0
        b.write(Int(flags))
        
        if self.id is not None:
            b.write(String(self.id))
        
        if self.shipping_options is not None:
            b.write(Vector(self.shipping_options))
        
        return b.getvalue()
