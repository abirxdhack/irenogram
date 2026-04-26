
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdatePersonalChannel(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``D94305E0``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel"]

    ID = 0xd94305e0
    QUALNAME = "functions.account.UpdatePersonalChannel"

    def __init__(self, *, channel: "raw.base.InputChannel") -> None:
        self.channel = channel

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePersonalChannel":
        
        channel = TLObject.read(b)
        
        return UpdatePersonalChannel(channel=channel)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.channel.write())
        
        return b.getvalue()
