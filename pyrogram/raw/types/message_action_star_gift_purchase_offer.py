
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageActionStarGiftPurchaseOffer(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``774278D4``

    Parameters:
        gift (:obj:`StarGift <pyrogram.raw.base.StarGift>`):
            N/A

        price (:obj:`StarsAmount <pyrogram.raw.base.StarsAmount>`):
            N/A

        expires_at (``int`` ``32-bit``):
            N/A

        accepted (``bool``, *optional*):
            N/A

        declined (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["gift", "price", "expires_at", "accepted", "declined"]

    ID = 0x774278d4
    QUALNAME = "types.MessageActionStarGiftPurchaseOffer"

    def __init__(self, *, gift: "raw.base.StarGift", price: "raw.base.StarsAmount", expires_at: int, accepted: Optional[bool] = None, declined: Optional[bool] = None) -> None:
        self.gift = gift
        self.price = price
        self.expires_at = expires_at
        self.accepted = accepted
        self.declined = declined

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionStarGiftPurchaseOffer":
        
        flags = Int.read(b)
        
        accepted = True if flags & (1 << 0) else False
        declined = True if flags & (1 << 1) else False
        gift = TLObject.read(b)
        
        price = TLObject.read(b)
        
        expires_at = Int.read(b)
        
        return MessageActionStarGiftPurchaseOffer(gift=gift, price=price, expires_at=expires_at, accepted=accepted, declined=declined)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.accepted else 0
        flags |= (1 << 1) if self.declined else 0
        b.write(Int(flags))
        
        b.write(self.gift.write())
        
        b.write(self.price.write())
        
        b.write(Int(self.expires_at))
        
        return b.getvalue()
