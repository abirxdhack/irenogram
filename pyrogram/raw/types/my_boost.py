
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MyBoost(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MyBoost`.

    Details:
        - Layer: ``224``
        - ID: ``C448415C``

    Parameters:
        slot (``int`` ``32-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        expires (``int`` ``32-bit``):
            N/A

        peer (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

        cooldown_until_date (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["slot", "date", "expires", "peer", "cooldown_until_date"]

    ID = 0xc448415c
    QUALNAME = "types.MyBoost"

    def __init__(self, *, slot: int, date: int, expires: int, peer: "raw.base.Peer" = None, cooldown_until_date: Optional[int] = None) -> None:
        self.slot = slot
        self.date = date
        self.expires = expires
        self.peer = peer
        self.cooldown_until_date = cooldown_until_date

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MyBoost":
        
        flags = Int.read(b)
        
        slot = Int.read(b)
        
        peer = TLObject.read(b) if flags & (1 << 0) else None
        
        date = Int.read(b)
        
        expires = Int.read(b)
        
        cooldown_until_date = Int.read(b) if flags & (1 << 1) else None
        return MyBoost(slot=slot, date=date, expires=expires, peer=peer, cooldown_until_date=cooldown_until_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.peer is not None else 0
        flags |= (1 << 1) if self.cooldown_until_date is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.slot))
        
        if self.peer is not None:
            b.write(self.peer.write())
        
        b.write(Int(self.date))
        
        b.write(Int(self.expires))
        
        if self.cooldown_until_date is not None:
            b.write(Int(self.cooldown_until_date))
        
        return b.getvalue()
