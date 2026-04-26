
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetChannels(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``A7F6BBB``

    Parameters:
        id (List of :obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

    Returns:
        :obj:`messages.Chats <pyrogram.raw.base.messages.Chats>`
    """

    __slots__: List[str] = ["id"]

    ID = 0xa7f6bbb
    QUALNAME = "functions.channels.GetChannels"

    def __init__(self, *, id: List["raw.base.InputChannel"]) -> None:
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetChannels":
        
        id = TLObject.read(b)
        
        return GetChannels(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.id))
        
        return b.getvalue()
