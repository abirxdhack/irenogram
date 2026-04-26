
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ToggleAntiSpam(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``68F3E4EB``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        enabled (``bool``):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "enabled"]

    ID = 0x68f3e4eb
    QUALNAME = "functions.channels.ToggleAntiSpam"

    def __init__(self, *, channel: "raw.base.InputChannel", enabled: bool) -> None:
        self.channel = channel
        self.enabled = enabled

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleAntiSpam":
        
        channel = TLObject.read(b)
        
        enabled = Bool.read(b)
        
        return ToggleAntiSpam(channel=channel, enabled=enabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.channel.write())
        
        b.write(Bool(self.enabled))
        
        return b.getvalue()
