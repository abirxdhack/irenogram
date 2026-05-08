
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateChannel(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``635B4C09``

    Parameters:
        channel_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["channel_id"]

    ID = 0x635b4c09
    QUALNAME = "types.UpdateChannel"

    def __init__(self, *, channel_id: int) -> None:
        self.channel_id = channel_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChannel":
        
        channel_id = Long.read(b)
        
        return UpdateChannel(channel_id=channel_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.channel_id))
        
        return b.getvalue()
