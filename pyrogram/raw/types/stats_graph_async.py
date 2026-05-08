
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class StatsGraphAsync(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StatsGraph`.

    Details:
        - Layer: ``224``
        - ID: ``4A27EB2D``

    Parameters:
        token (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stats.LoadAsyncGraph
    """

    __slots__: List[str] = ["token"]

    ID = 0x4a27eb2d
    QUALNAME = "types.StatsGraphAsync"

    def __init__(self, *, token: str) -> None:
        self.token = token

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StatsGraphAsync":
        
        token = String.read(b)
        
        return StatsGraphAsync(token=token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.token))
        
        return b.getvalue()
