
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InlineQueryPeerTypeSameBotPM(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InlineQueryPeerType`.

    Details:
        - Layer: ``224``
        - ID: ``3081ED9D``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x3081ed9d
    QUALNAME = "types.InlineQueryPeerTypeSameBotPM"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InlineQueryPeerTypeSameBotPM":
        
        return InlineQueryPeerTypeSameBotPM()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
