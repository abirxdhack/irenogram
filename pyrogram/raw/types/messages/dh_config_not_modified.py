
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DhConfigNotModified(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.DhConfig`.

    Details:
        - Layer: ``224``
        - ID: ``C0E24635``

    Parameters:
        random (``bytes``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetDhConfig
    """

    __slots__: List[str] = ["random"]

    ID = 0xc0e24635
    QUALNAME = "types.messages.DhConfigNotModified"

    def __init__(self, *, random: bytes) -> None:
        self.random = random

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DhConfigNotModified":
        
        random = Bytes.read(b)
        
        return DhConfigNotModified(random=random)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Bytes(self.random))
        
        return b.getvalue()
