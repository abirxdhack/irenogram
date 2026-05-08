
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ToggleJoinRequest(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``4C2985B6``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        enabled (``bool``):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "enabled"]

    ID = 0x4c2985b6
    QUALNAME = "functions.channels.ToggleJoinRequest"

    def __init__(self, *, channel: "raw.base.InputChannel", enabled: bool) -> None:
        self.channel = channel
        self.enabled = enabled

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleJoinRequest":
        
        channel = TLObject.read(b)
        
        enabled = Bool.read(b)
        
        return ToggleJoinRequest(channel=channel, enabled=enabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.channel.write())
        
        b.write(Bool(self.enabled))
        
        return b.getvalue()
