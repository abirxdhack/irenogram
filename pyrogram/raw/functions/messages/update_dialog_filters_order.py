
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateDialogFiltersOrder(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``C563C1E4``

    Parameters:
        order (List of ``int`` ``32-bit``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["order"]

    ID = 0xc563c1e4
    QUALNAME = "functions.messages.UpdateDialogFiltersOrder"

    def __init__(self, *, order: List[int]) -> None:
        self.order = order

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateDialogFiltersOrder":
        
        order = TLObject.read(b, Int)
        
        return UpdateDialogFiltersOrder(order=order)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.order, Int))
        
        return b.getvalue()
