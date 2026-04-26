
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelLocationEmpty(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelLocation`.

    Details:
        - Layer: ``224``
        - ID: ``BFB5AD8B``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xbfb5ad8b
    QUALNAME = "types.ChannelLocationEmpty"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelLocationEmpty":
        
        return ChannelLocationEmpty()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
