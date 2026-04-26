
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PeerColorSet(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.help.PeerColorSet`.

    Details:
        - Layer: ``224``
        - ID: ``26219A58``

    Parameters:
        colors (List of ``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["colors"]

    ID = 0x26219a58
    QUALNAME = "types.help.PeerColorSet"

    def __init__(self, *, colors: List[int]) -> None:
        self.colors = colors

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerColorSet":
        
        colors = TLObject.read(b, Int)
        
        return PeerColorSet(colors=colors)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.colors, Int))
        
        return b.getvalue()
