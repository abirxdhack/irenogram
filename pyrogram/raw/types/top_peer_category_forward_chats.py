
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class TopPeerCategoryForwardChats(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.TopPeerCategory`.

    Details:
        - Layer: ``224``
        - ID: ``FBEEC0F0``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xfbeec0f0
    QUALNAME = "types.TopPeerCategoryForwardChats"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TopPeerCategoryForwardChats":
        
        return TopPeerCategoryForwardChats()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
