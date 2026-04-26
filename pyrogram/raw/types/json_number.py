
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class JsonNumber(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.JSONValue`.

    Details:
        - Layer: ``224``
        - ID: ``2BE0DFA4``

    Parameters:
        value (``float`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["value"]

    ID = 0x2be0dfa4
    QUALNAME = "types.JsonNumber"

    def __init__(self, *, value: float) -> None:
        self.value = value

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "JsonNumber":
        
        value = Double.read(b)
        
        return JsonNumber(value=value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Double(self.value))
        
        return b.getvalue()
