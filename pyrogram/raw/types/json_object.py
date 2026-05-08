
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class JsonObject(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.JSONValue`.

    Details:
        - Layer: ``224``
        - ID: ``99C1D49D``

    Parameters:
        value (List of :obj:`JSONObjectValue <pyrogram.raw.base.JSONObjectValue>`):
            N/A

    """

    __slots__: List[str] = ["value"]

    ID = 0x99c1d49d
    QUALNAME = "types.JsonObject"

    def __init__(self, *, value: List["raw.base.JSONObjectValue"]) -> None:
        self.value = value

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "JsonObject":
        
        value = TLObject.read(b)
        
        return JsonObject(value=value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.value))
        
        return b.getvalue()
