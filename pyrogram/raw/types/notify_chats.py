
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class NotifyChats(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.NotifyPeer`.

    Details:
        - Layer: ``224``
        - ID: ``C007CEC3``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xc007cec3
    QUALNAME = "types.NotifyChats"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "NotifyChats":
        
        return NotifyChats()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
