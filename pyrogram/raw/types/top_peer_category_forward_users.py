
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class TopPeerCategoryForwardUsers(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.TopPeerCategory`.

    Details:
        - Layer: ``224``
        - ID: ``A8406CA9``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xa8406ca9
    QUALNAME = "types.TopPeerCategoryForwardUsers"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TopPeerCategoryForwardUsers":
        
        return TopPeerCategoryForwardUsers()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
