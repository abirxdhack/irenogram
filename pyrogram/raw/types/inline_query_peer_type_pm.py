
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InlineQueryPeerTypePM(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InlineQueryPeerType`.

    Details:
        - Layer: ``224``
        - ID: ``833C0FAC``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x833c0fac
    QUALNAME = "types.InlineQueryPeerTypePM"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InlineQueryPeerTypePM":
        
        return InlineQueryPeerTypePM()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
