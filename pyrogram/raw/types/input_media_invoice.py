
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputMediaInvoice(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``224``
        - ID: ``405FEF0D``

    Parameters:
        title (``str``):
            N/A

        description (``str``):
            N/A

        invoice (:obj:`Invoice <pyrogram.raw.base.Invoice>`):
            N/A

        payload (``bytes``):
            N/A

        provider_data (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`):
            N/A

        photo (:obj:`InputWebDocument <pyrogram.raw.base.InputWebDocument>`, *optional*):
            N/A

        provider (``str``, *optional*):
            N/A

        start_param (``str``, *optional*):
            N/A

        extended_media (:obj:`InputMedia <pyrogram.raw.base.InputMedia>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["title", "description", "invoice", "payload", "provider_data", "photo", "provider", "start_param", "extended_media"]

    ID = 0x405fef0d
    QUALNAME = "types.InputMediaInvoice"

    def __init__(self, *, title: str, description: str, invoice: "raw.base.Invoice", payload: bytes, provider_data: "raw.base.DataJSON", photo: "raw.base.InputWebDocument" = None, provider: Optional[str] = None, start_param: Optional[str] = None, extended_media: "raw.base.InputMedia" = None) -> None:
        self.title = title
        self.description = description
        self.invoice = invoice
        self.payload = payload
        self.provider_data = provider_data
        self.photo = photo
        self.provider = provider
        self.start_param = start_param
        self.extended_media = extended_media

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaInvoice":
        
        flags = Int.read(b)
        
        title = String.read(b)
        
        description = String.read(b)
        
        photo = TLObject.read(b) if flags & (1 << 0) else None
        
        invoice = TLObject.read(b)
        
        payload = Bytes.read(b)
        
        provider = String.read(b) if flags & (1 << 3) else None
        provider_data = TLObject.read(b)
        
        start_param = String.read(b) if flags & (1 << 1) else None
        extended_media = TLObject.read(b) if flags & (1 << 2) else None
        
        return InputMediaInvoice(title=title, description=description, invoice=invoice, payload=payload, provider_data=provider_data, photo=photo, provider=provider, start_param=start_param, extended_media=extended_media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.photo is not None else 0
        flags |= (1 << 3) if self.provider is not None else 0
        flags |= (1 << 1) if self.start_param is not None else 0
        flags |= (1 << 2) if self.extended_media is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.title))
        
        b.write(String(self.description))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        b.write(self.invoice.write())
        
        b.write(Bytes(self.payload))
        
        if self.provider is not None:
            b.write(String(self.provider))
        
        b.write(self.provider_data.write())
        
        if self.start_param is not None:
            b.write(String(self.start_param))
        
        if self.extended_media is not None:
            b.write(self.extended_media.write())
        
        return b.getvalue()
