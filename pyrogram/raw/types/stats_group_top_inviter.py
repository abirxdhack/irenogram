
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class StatsGroupTopInviter(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StatsGroupTopInviter`.

    Details:
        - Layer: ``224``
        - ID: ``535F779D``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        invitations (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["user_id", "invitations"]

    ID = 0x535f779d
    QUALNAME = "types.StatsGroupTopInviter"

    def __init__(self, *, user_id: int, invitations: int) -> None:
        self.user_id = user_id
        self.invitations = invitations

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StatsGroupTopInviter":
        
        user_id = Long.read(b)
        
        invitations = Int.read(b)
        
        return StatsGroupTopInviter(user_id=user_id, invitations=invitations)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.user_id))
        
        b.write(Int(self.invitations))
        
        return b.getvalue()
