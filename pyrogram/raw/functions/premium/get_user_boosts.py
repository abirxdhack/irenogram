
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetUserBoosts(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``39854D1F``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

    Returns:
        :obj:`premium.BoostsList <pyrogram.raw.base.premium.BoostsList>`
    """

    __slots__: List[str] = ["peer", "user_id"]

    ID = 0x39854d1f
    QUALNAME = "functions.premium.GetUserBoosts"

    def __init__(self, *, peer: "raw.base.InputPeer", user_id: "raw.base.InputUser") -> None:
        self.peer = peer
        self.user_id = user_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetUserBoosts":
        
        peer = TLObject.read(b)
        
        user_id = TLObject.read(b)
        
        return GetUserBoosts(peer=peer, user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(self.user_id.write())
        
        return b.getvalue()
