
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class TopPeerCategoryBotsPM(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.TopPeerCategory`.

    Details:
        - Layer: ``224``
        - ID: ``AB661B5B``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xab661b5b
    QUALNAME = "types.TopPeerCategoryBotsPM"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TopPeerCategoryBotsPM":
        
        return TopPeerCategoryBotsPM()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
