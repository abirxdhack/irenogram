
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class CheckUsername(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``10E6BD2C``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        username (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel", "username"]

    ID = 0x10e6bd2c
    QUALNAME = "functions.channels.CheckUsername"

    def __init__(self, *, channel: "raw.base.InputChannel", username: str) -> None:
        self.channel = channel
        self.username = username

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckUsername":
        
        channel = TLObject.read(b)
        
        username = String.read(b)
        
        return CheckUsername(channel=channel, username=username)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.channel.write())
        
        b.write(String(self.username))
        
        return b.getvalue()
