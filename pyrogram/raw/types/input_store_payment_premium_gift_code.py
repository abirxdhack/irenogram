
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputStorePaymentPremiumGiftCode(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputStorePaymentPurpose`.

    Details:
        - Layer: ``224``
        - ID: ``FB790393``

    Parameters:
        users (List of :obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        currency (``str``):
            N/A

        amount (``int`` ``64-bit``):
            N/A

        boost_peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

        message (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["users", "currency", "amount", "boost_peer", "message"]

    ID = 0xfb790393
    QUALNAME = "types.InputStorePaymentPremiumGiftCode"

    def __init__(self, *, users: List["raw.base.InputUser"], currency: str, amount: int, boost_peer: "raw.base.InputPeer" = None, message: "raw.base.TextWithEntities" = None) -> None:
        self.users = users
        self.currency = currency
        self.amount = amount
        self.boost_peer = boost_peer
        self.message = message

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStorePaymentPremiumGiftCode":
        
        flags = Int.read(b)
        
        users = TLObject.read(b)
        
        boost_peer = TLObject.read(b) if flags & (1 << 0) else None
        
        currency = String.read(b)
        
        amount = Long.read(b)
        
        message = TLObject.read(b) if flags & (1 << 1) else None
        
        return InputStorePaymentPremiumGiftCode(users=users, currency=currency, amount=amount, boost_peer=boost_peer, message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.boost_peer is not None else 0
        flags |= (1 << 1) if self.message is not None else 0
        b.write(Int(flags))
        
        b.write(Vector(self.users))
        
        if self.boost_peer is not None:
            b.write(self.boost_peer.write())
        
        b.write(String(self.currency))
        
        b.write(Long(self.amount))
        
        if self.message is not None:
            b.write(self.message.write())
        
        return b.getvalue()
