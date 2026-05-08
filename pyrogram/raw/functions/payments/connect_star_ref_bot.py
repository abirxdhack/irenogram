
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ConnectStarRefBot(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``7ED5348A``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

    Returns:
        :obj:`payments.ConnectedStarRefBots <pyrogram.raw.base.payments.ConnectedStarRefBots>`
    """

    __slots__: List[str] = ["peer", "bot"]

    ID = 0x7ed5348a
    QUALNAME = "functions.payments.ConnectStarRefBot"

    def __init__(self, *, peer: "raw.base.InputPeer", bot: "raw.base.InputUser") -> None:
        self.peer = peer
        self.bot = bot

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ConnectStarRefBot":
        
        peer = TLObject.read(b)
        
        bot = TLObject.read(b)
        
        return ConnectStarRefBot(peer=peer, bot=bot)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(self.bot.write())
        
        return b.getvalue()
