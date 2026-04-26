
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ReorderUsernames(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``EF500EAB``

    Parameters:
        order (List of ``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["order"]

    ID = 0xef500eab
    QUALNAME = "functions.account.ReorderUsernames"

    def __init__(self, *, order: List[str]) -> None:
        self.order = order

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReorderUsernames":
        
        order = TLObject.read(b, String)
        
        return ReorderUsernames(order=order)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.order, String))
        
        return b.getvalue()
