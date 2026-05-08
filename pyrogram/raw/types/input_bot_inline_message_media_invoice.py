
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputBotInlineMessageMediaInvoice(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputBotInlineMessage`.

    Details:
        - Layer: ``224``
        - ID: ``D7E78225``

    Parameters:
        title (``str``):
            N/A

        description (``str``):
            N/A

        invoice (:obj:`Invoice <pyrogram.raw.base.Invoice>`):
            N/A

        payload (``bytes``):
            N/A

        provider (``str``):
            N/A

        provider_data (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`):
            N/A

        photo (:obj:`InputWebDocument <pyrogram.raw.base.InputWebDocument>`, *optional*):
            N/A

        reply_markup (:obj:`ReplyMarkup <pyrogram.raw.base.ReplyMarkup>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["title", "description", "invoice", "payload", "provider", "provider_data", "photo", "reply_markup"]

    ID = 0xd7e78225
    QUALNAME = "types.InputBotInlineMessageMediaInvoice"

    def __init__(self, *, title: str, description: str, invoice: "raw.base.Invoice", payload: bytes, provider: str, provider_data: "raw.base.DataJSON", photo: "raw.base.InputWebDocument" = None, reply_markup: "raw.base.ReplyMarkup" = None) -> None:
        self.title = title
        self.description = description
        self.invoice = invoice
        self.payload = payload
        self.provider = provider
        self.provider_data = provider_data
        self.photo = photo
        self.reply_markup = reply_markup

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBotInlineMessageMediaInvoice":
        
        flags = Int.read(b)
        
        title = String.read(b)
        
        description = String.read(b)
        
        photo = TLObject.read(b) if flags & (1 << 0) else None
        
        invoice = TLObject.read(b)
        
        payload = Bytes.read(b)
        
        provider = String.read(b)
        
        provider_data = TLObject.read(b)
        
        reply_markup = TLObject.read(b) if flags & (1 << 2) else None
        
        return InputBotInlineMessageMediaInvoice(title=title, description=description, invoice=invoice, payload=payload, provider=provider, provider_data=provider_data, photo=photo, reply_markup=reply_markup)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.photo is not None else 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.title))
        
        b.write(String(self.description))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        b.write(self.invoice.write())
        
        b.write(Bytes(self.payload))
        
        b.write(String(self.provider))
        
        b.write(self.provider_data.write())
        
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        
        return b.getvalue()
