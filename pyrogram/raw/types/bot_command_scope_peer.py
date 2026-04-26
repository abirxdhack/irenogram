
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class BotCommandScopePeer(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BotCommandScope`.

    Details:
        - Layer: ``224``
        - ID: ``DB9D897D``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

    """

    __slots__: List[str] = ["peer"]

    ID = 0xdb9d897d
    QUALNAME = "types.BotCommandScopePeer"

    def __init__(self, *, peer: "raw.base.InputPeer") -> None:
        self.peer = peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotCommandScopePeer":
        
        peer = TLObject.read(b)
        
        return BotCommandScopePeer(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        return b.getvalue()
