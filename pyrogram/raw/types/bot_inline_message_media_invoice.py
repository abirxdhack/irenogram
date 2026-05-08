
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class BotInlineMessageMediaInvoice(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BotInlineMessage`.

    Details:
        - Layer: ``224``
        - ID: ``354A9B09``

    Parameters:
        title (``str``):
            N/A

        description (``str``):
            N/A

        currency (``str``):
            N/A

        total_amount (``int`` ``64-bit``):
            N/A

        shipping_address_requested (``bool``, *optional*):
            N/A

        test (``bool``, *optional*):
            N/A

        photo (:obj:`WebDocument <pyrogram.raw.base.WebDocument>`, *optional*):
            N/A

        reply_markup (:obj:`ReplyMarkup <pyrogram.raw.base.ReplyMarkup>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["title", "description", "currency", "total_amount", "shipping_address_requested", "test", "photo", "reply_markup"]

    ID = 0x354a9b09
    QUALNAME = "types.BotInlineMessageMediaInvoice"

    def __init__(self, *, title: str, description: str, currency: str, total_amount: int, shipping_address_requested: Optional[bool] = None, test: Optional[bool] = None, photo: "raw.base.WebDocument" = None, reply_markup: "raw.base.ReplyMarkup" = None) -> None:
        self.title = title
        self.description = description
        self.currency = currency
        self.total_amount = total_amount
        self.shipping_address_requested = shipping_address_requested
        self.test = test
        self.photo = photo
        self.reply_markup = reply_markup

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotInlineMessageMediaInvoice":
        
        flags = Int.read(b)
        
        shipping_address_requested = True if flags & (1 << 1) else False
        test = True if flags & (1 << 3) else False
        title = String.read(b)
        
        description = String.read(b)
        
        photo = TLObject.read(b) if flags & (1 << 0) else None
        
        currency = String.read(b)
        
        total_amount = Long.read(b)
        
        reply_markup = TLObject.read(b) if flags & (1 << 2) else None
        
        return BotInlineMessageMediaInvoice(title=title, description=description, currency=currency, total_amount=total_amount, shipping_address_requested=shipping_address_requested, test=test, photo=photo, reply_markup=reply_markup)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.shipping_address_requested else 0
        flags |= (1 << 3) if self.test else 0
        flags |= (1 << 0) if self.photo is not None else 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.title))
        
        b.write(String(self.description))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        b.write(String(self.currency))
        
        b.write(Long(self.total_amount))
        
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        
        return b.getvalue()
