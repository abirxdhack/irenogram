
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SearchResultsPositions(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.SearchResultsPositions`.

    Details:
        - Layer: ``224``
        - ID: ``53B22BAF``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        positions (List of :obj:`SearchResultsPosition <pyrogram.raw.base.SearchResultsPosition>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSearchResultsPositions
    """

    __slots__: List[str] = ["count", "positions"]

    ID = 0x53b22baf
    QUALNAME = "types.messages.SearchResultsPositions"

    def __init__(self, *, count: int, positions: List["raw.base.SearchResultsPosition"]) -> None:
        self.count = count
        self.positions = positions

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SearchResultsPositions":
        
        count = Int.read(b)
        
        positions = TLObject.read(b)
        
        return SearchResultsPositions(count=count, positions=positions)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.count))
        
        b.write(Vector(self.positions))
        
        return b.getvalue()
