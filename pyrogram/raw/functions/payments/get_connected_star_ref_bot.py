
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetConnectedStarRefBot(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``B7D998F0``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

    Returns:
        :obj:`payments.ConnectedStarRefBots <pyrogram.raw.base.payments.ConnectedStarRefBots>`
    """

    __slots__: List[str] = ["peer", "bot"]

    ID = 0xb7d998f0
    QUALNAME = "functions.payments.GetConnectedStarRefBot"

    def __init__(self, *, peer: "raw.base.InputPeer", bot: "raw.base.InputUser") -> None:
        self.peer = peer
        self.bot = bot

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetConnectedStarRefBot":
        
        peer = TLObject.read(b)
        
        bot = TLObject.read(b)
        
        return GetConnectedStarRefBot(peer=peer, bot=bot)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(self.bot.write())
        
        return b.getvalue()
