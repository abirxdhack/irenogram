
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SetBoostsToUnblockRestrictions(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``AD399CEE``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        boosts (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "boosts"]

    ID = 0xad399cee
    QUALNAME = "functions.channels.SetBoostsToUnblockRestrictions"

    def __init__(self, *, channel: "raw.base.InputChannel", boosts: int) -> None:
        self.channel = channel
        self.boosts = boosts

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetBoostsToUnblockRestrictions":
        
        channel = TLObject.read(b)
        
        boosts = Int.read(b)
        
        return SetBoostsToUnblockRestrictions(channel=channel, boosts=boosts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.channel.write())
        
        b.write(Int(self.boosts))
        
        return b.getvalue()
