
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ReportMusicListen(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``DDBCD819``

    Parameters:
        id (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`):
            N/A

        listened_duration (``int`` ``32-bit``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id", "listened_duration"]

    ID = 0xddbcd819
    QUALNAME = "functions.messages.ReportMusicListen"

    def __init__(self, *, id: "raw.base.InputDocument", listened_duration: int) -> None:
        self.id = id
        self.listened_duration = listened_duration

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportMusicListen":
        
        id = TLObject.read(b)
        
        listened_duration = Int.read(b)
        
        return ReportMusicListen(id=id, listened_duration=listened_duration)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.id.write())
        
        b.write(Int(self.listened_duration))
        
        return b.getvalue()
