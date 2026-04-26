
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SetBotShippingResults(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``E5F672FA``

    Parameters:
        query_id (``int`` ``64-bit``):
            N/A

        error (``str``, *optional*):
            N/A

        shipping_options (List of :obj:`ShippingOption <pyrogram.raw.base.ShippingOption>`, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["query_id", "error", "shipping_options"]

    ID = 0xe5f672fa
    QUALNAME = "functions.messages.SetBotShippingResults"

    def __init__(self, *, query_id: int, error: Optional[str] = None, shipping_options: Optional[List["raw.base.ShippingOption"]] = None) -> None:
        self.query_id = query_id
        self.error = error
        self.shipping_options = shipping_options

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetBotShippingResults":
        
        flags = Int.read(b)
        
        query_id = Long.read(b)
        
        error = String.read(b) if flags & (1 << 0) else None
        shipping_options = TLObject.read(b) if flags & (1 << 1) else []
        
        return SetBotShippingResults(query_id=query_id, error=error, shipping_options=shipping_options)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.error is not None else 0
        flags |= (1 << 1) if self.shipping_options else 0
        b.write(Int(flags))
        
        b.write(Long(self.query_id))
        
        if self.error is not None:
            b.write(String(self.error))
        
        if self.shipping_options is not None:
            b.write(Vector(self.shipping_options))
        
        return b.getvalue()
