
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ConnectedStarRefBots(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.ConnectedStarRefBots`.

    Details:
        - Layer: ``224``
        - ID: ``98D5EA1D``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        connected_bots (List of :obj:`ConnectedBotStarRef <pyrogram.raw.base.ConnectedBotStarRef>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 4 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetConnectedStarRefBots
            payments.GetConnectedStarRefBot
            payments.ConnectStarRefBot
            payments.EditConnectedStarRefBot
    """

    __slots__: List[str] = ["count", "connected_bots", "users"]

    ID = 0x98d5ea1d
    QUALNAME = "types.payments.ConnectedStarRefBots"

    def __init__(self, *, count: int, connected_bots: List["raw.base.ConnectedBotStarRef"], users: List["raw.base.User"]) -> None:
        self.count = count
        self.connected_bots = connected_bots
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ConnectedStarRefBots":
        
        count = Int.read(b)
        
        connected_bots = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return ConnectedStarRefBots(count=count, connected_bots=connected_bots, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.count))
        
        b.write(Vector(self.connected_bots))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
