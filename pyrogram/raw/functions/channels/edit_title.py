
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EditTitle(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``566DECD0``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        title (``str``):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "title"]

    ID = 0x566decd0
    QUALNAME = "functions.channels.EditTitle"

    def __init__(self, *, channel: "raw.base.InputChannel", title: str) -> None:
        self.channel = channel
        self.title = title

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditTitle":
        
        channel = TLObject.read(b)
        
        title = String.read(b)
        
        return EditTitle(channel=channel, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.channel.write())
        
        b.write(String(self.title))
        
        return b.getvalue()
