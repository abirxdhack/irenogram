
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class BotCommandScopePeerUser(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BotCommandScope`.

    Details:
        - Layer: ``224``
        - ID: ``A1321F3``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

    """

    __slots__: List[str] = ["peer", "user_id"]

    ID = 0xa1321f3
    QUALNAME = "types.BotCommandScopePeerUser"

    def __init__(self, *, peer: "raw.base.InputPeer", user_id: "raw.base.InputUser") -> None:
        self.peer = peer
        self.user_id = user_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotCommandScopePeerUser":
        
        peer = TLObject.read(b)
        
        user_id = TLObject.read(b)
        
        return BotCommandScopePeerUser(peer=peer, user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(self.user_id.write())
        
        return b.getvalue()
