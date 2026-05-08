
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DeleteHistory(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``9BAA9647``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        max_id (``int`` ``32-bit``):
            N/A

        for_everyone (``bool``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "max_id", "for_everyone"]

    ID = 0x9baa9647
    QUALNAME = "functions.channels.DeleteHistory"

    def __init__(self, *, channel: "raw.base.InputChannel", max_id: int, for_everyone: Optional[bool] = None) -> None:
        self.channel = channel
        self.max_id = max_id
        self.for_everyone = for_everyone

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteHistory":
        
        flags = Int.read(b)
        
        for_everyone = True if flags & (1 << 0) else False
        channel = TLObject.read(b)
        
        max_id = Int.read(b)
        
        return DeleteHistory(channel=channel, max_id=max_id, for_everyone=for_everyone)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.for_everyone else 0
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        b.write(Int(self.max_id))
        
        return b.getvalue()
