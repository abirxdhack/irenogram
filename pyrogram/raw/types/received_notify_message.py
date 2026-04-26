
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ReceivedNotifyMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ReceivedNotifyMessage`.

    Details:
        - Layer: ``224``
        - ID: ``A384B779``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

        flags (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.ReceivedMessages
    """

    __slots__: List[str] = ["id", "flags"]

    ID = 0xa384b779
    QUALNAME = "types.ReceivedNotifyMessage"

    def __init__(self, *, id: int, flags: int) -> None:
        self.id = id
        self.flags = flags

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReceivedNotifyMessage":
        
        id = Int.read(b)
        
        flags = Int.read(b)
        
        return ReceivedNotifyMessage(id=id, flags=flags)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.id))
        
        b.write(Int(self.flags))
        
        return b.getvalue()
