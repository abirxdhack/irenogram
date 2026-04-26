
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ToggleViewForumAsMessages(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``9738BB15``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        enabled (``bool``):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "enabled"]

    ID = 0x9738bb15
    QUALNAME = "functions.channels.ToggleViewForumAsMessages"

    def __init__(self, *, channel: "raw.base.InputChannel", enabled: bool) -> None:
        self.channel = channel
        self.enabled = enabled

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleViewForumAsMessages":
        
        channel = TLObject.read(b)
        
        enabled = Bool.read(b)
        
        return ToggleViewForumAsMessages(channel=channel, enabled=enabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.channel.write())
        
        b.write(Bool(self.enabled))
        
        return b.getvalue()
