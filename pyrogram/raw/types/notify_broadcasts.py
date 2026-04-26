
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class NotifyBroadcasts(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.NotifyPeer`.

    Details:
        - Layer: ``224``
        - ID: ``D612E8EF``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xd612e8ef
    QUALNAME = "types.NotifyBroadcasts"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "NotifyBroadcasts":
        
        return NotifyBroadcasts()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
