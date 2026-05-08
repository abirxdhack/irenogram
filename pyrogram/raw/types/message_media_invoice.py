
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageMediaInvoice(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``224``
        - ID: ``F6A548D3``

    Parameters:
        title (``str``):
            N/A

        description (``str``):
            N/A

        currency (``str``):
            N/A

        total_amount (``int`` ``64-bit``):
            N/A

        start_param (``str``):
            N/A

        shipping_address_requested (``bool``, *optional*):
            N/A

        test (``bool``, *optional*):
            N/A

        photo (:obj:`WebDocument <pyrogram.raw.base.WebDocument>`, *optional*):
            N/A

        receipt_msg_id (``int`` ``32-bit``, *optional*):
            N/A

        extended_media (:obj:`MessageExtendedMedia <pyrogram.raw.base.MessageExtendedMedia>`, *optional*):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: List[str] = ["title", "description", "currency", "total_amount", "start_param", "shipping_address_requested", "test", "photo", "receipt_msg_id", "extended_media"]

    ID = 0xf6a548d3
    QUALNAME = "types.MessageMediaInvoice"

    def __init__(self, *, title: str, description: str, currency: str, total_amount: int, start_param: str, shipping_address_requested: Optional[bool] = None, test: Optional[bool] = None, photo: "raw.base.WebDocument" = None, receipt_msg_id: Optional[int] = None, extended_media: "raw.base.MessageExtendedMedia" = None) -> None:
        self.title = title
        self.description = description
        self.currency = currency
        self.total_amount = total_amount
        self.start_param = start_param
        self.shipping_address_requested = shipping_address_requested
        self.test = test
        self.photo = photo
        self.receipt_msg_id = receipt_msg_id
        self.extended_media = extended_media

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaInvoice":
        
        flags = Int.read(b)
        
        shipping_address_requested = True if flags & (1 << 1) else False
        test = True if flags & (1 << 3) else False
        title = String.read(b)
        
        description = String.read(b)
        
        photo = TLObject.read(b) if flags & (1 << 0) else None
        
        receipt_msg_id = Int.read(b) if flags & (1 << 2) else None
        currency = String.read(b)
        
        total_amount = Long.read(b)
        
        start_param = String.read(b)
        
        extended_media = TLObject.read(b) if flags & (1 << 4) else None
        
        return MessageMediaInvoice(title=title, description=description, currency=currency, total_amount=total_amount, start_param=start_param, shipping_address_requested=shipping_address_requested, test=test, photo=photo, receipt_msg_id=receipt_msg_id, extended_media=extended_media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.shipping_address_requested else 0
        flags |= (1 << 3) if self.test else 0
        flags |= (1 << 0) if self.photo is not None else 0
        flags |= (1 << 2) if self.receipt_msg_id is not None else 0
        flags |= (1 << 4) if self.extended_media is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.title))
        
        b.write(String(self.description))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        if self.receipt_msg_id is not None:
            b.write(Int(self.receipt_msg_id))
        
        b.write(String(self.currency))
        
        b.write(Long(self.total_amount))
        
        b.write(String(self.start_param))
        
        if self.extended_media is not None:
            b.write(self.extended_media.write())
        
        return b.getvalue()
