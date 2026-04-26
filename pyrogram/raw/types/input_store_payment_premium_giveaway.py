
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputStorePaymentPremiumGiveaway(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputStorePaymentPurpose`.

    Details:
        - Layer: ``224``
        - ID: ``160544CA``

    Parameters:
        boost_peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        random_id (``int`` ``64-bit``):
            N/A

        until_date (``int`` ``32-bit``):
            N/A

        currency (``str``):
            N/A

        amount (``int`` ``64-bit``):
            N/A

        only_new_subscribers (``bool``, *optional*):
            N/A

        winners_are_visible (``bool``, *optional*):
            N/A

        additional_peers (List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

        countries_iso2 (List of ``str``, *optional*):
            N/A

        prize_description (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["boost_peer", "random_id", "until_date", "currency", "amount", "only_new_subscribers", "winners_are_visible", "additional_peers", "countries_iso2", "prize_description"]

    ID = 0x160544ca
    QUALNAME = "types.InputStorePaymentPremiumGiveaway"

    def __init__(self, *, boost_peer: "raw.base.InputPeer", random_id: int, until_date: int, currency: str, amount: int, only_new_subscribers: Optional[bool] = None, winners_are_visible: Optional[bool] = None, additional_peers: Optional[List["raw.base.InputPeer"]] = None, countries_iso2: Optional[List[str]] = None, prize_description: Optional[str] = None) -> None:
        self.boost_peer = boost_peer
        self.random_id = random_id
        self.until_date = until_date
        self.currency = currency
        self.amount = amount
        self.only_new_subscribers = only_new_subscribers
        self.winners_are_visible = winners_are_visible
        self.additional_peers = additional_peers
        self.countries_iso2 = countries_iso2
        self.prize_description = prize_description

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStorePaymentPremiumGiveaway":
        
        flags = Int.read(b)
        
        only_new_subscribers = True if flags & (1 << 0) else False
        winners_are_visible = True if flags & (1 << 3) else False
        boost_peer = TLObject.read(b)
        
        additional_peers = TLObject.read(b) if flags & (1 << 1) else []
        
        countries_iso2 = TLObject.read(b, String) if flags & (1 << 2) else []
        
        prize_description = String.read(b) if flags & (1 << 4) else None
        random_id = Long.read(b)
        
        until_date = Int.read(b)
        
        currency = String.read(b)
        
        amount = Long.read(b)
        
        return InputStorePaymentPremiumGiveaway(boost_peer=boost_peer, random_id=random_id, until_date=until_date, currency=currency, amount=amount, only_new_subscribers=only_new_subscribers, winners_are_visible=winners_are_visible, additional_peers=additional_peers, countries_iso2=countries_iso2, prize_description=prize_description)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.only_new_subscribers else 0
        flags |= (1 << 3) if self.winners_are_visible else 0
        flags |= (1 << 1) if self.additional_peers else 0
        flags |= (1 << 2) if self.countries_iso2 else 0
        flags |= (1 << 4) if self.prize_description is not None else 0
        b.write(Int(flags))
        
        b.write(self.boost_peer.write())
        
        if self.additional_peers is not None:
            b.write(Vector(self.additional_peers))
        
        if self.countries_iso2 is not None:
            b.write(Vector(self.countries_iso2, String))
        
        if self.prize_description is not None:
            b.write(String(self.prize_description))
        
        b.write(Long(self.random_id))
        
        b.write(Int(self.until_date))
        
        b.write(String(self.currency))
        
        b.write(Long(self.amount))
        
        return b.getvalue()
