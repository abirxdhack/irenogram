
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class JsonString(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.JSONValue`.

    Details:
        - Layer: ``224``
        - ID: ``B71E767A``

    Parameters:
        value (``str``):
            N/A

    """

    __slots__: List[str] = ["value"]

    ID = 0xb71e767a
    QUALNAME = "types.JsonString"

    def __init__(self, *, value: str) -> None:
        self.value = value

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "JsonString":
        
        value = String.read(b)
        
        return JsonString(value=value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.value))
        
        return b.getvalue()
