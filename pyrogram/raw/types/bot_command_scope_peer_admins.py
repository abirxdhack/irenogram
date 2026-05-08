
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class BotCommandScopePeerAdmins(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BotCommandScope`.

    Details:
        - Layer: ``224``
        - ID: ``3FD863D1``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

    """

    __slots__: List[str] = ["peer"]

    ID = 0x3fd863d1
    QUALNAME = "types.BotCommandScopePeerAdmins"

    def __init__(self, *, peer: "raw.base.InputPeer") -> None:
        self.peer = peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotCommandScopePeerAdmins":
        
        peer = TLObject.read(b)
        
        return BotCommandScopePeerAdmins(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        return b.getvalue()
