
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ToggleForum(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``3FF75734``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        enabled (``bool``):
            N/A

        tabs (``bool``):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "enabled", "tabs"]

    ID = 0x3ff75734
    QUALNAME = "functions.channels.ToggleForum"

    def __init__(self, *, channel: "raw.base.InputChannel", enabled: bool, tabs: bool) -> None:
        self.channel = channel
        self.enabled = enabled
        self.tabs = tabs

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleForum":
        
        channel = TLObject.read(b)
        
        enabled = Bool.read(b)
        
        tabs = Bool.read(b)
        
        return ToggleForum(channel=channel, enabled=enabled, tabs=tabs)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.channel.write())
        
        b.write(Bool(self.enabled))
        
        b.write(Bool(self.tabs))
        
        return b.getvalue()
