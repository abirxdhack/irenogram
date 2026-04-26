
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PageBlockChannel(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``224``
        - ID: ``EF1751B5``

    Parameters:
        channel (:obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

    """

    __slots__: List[str] = ["channel"]

    ID = 0xef1751b5
    QUALNAME = "types.PageBlockChannel"

    def __init__(self, *, channel: "raw.base.Chat") -> None:
        self.channel = channel

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockChannel":
        
        channel = TLObject.read(b)
        
        return PageBlockChannel(channel=channel)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.channel.write())
        
        return b.getvalue()
