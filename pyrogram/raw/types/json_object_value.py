
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class JsonObjectValue(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.JSONObjectValue`.

    Details:
        - Layer: ``224``
        - ID: ``C0DE1BD9``

    Parameters:
        key (``str``):
            N/A

        value (:obj:`JSONValue <pyrogram.raw.base.JSONValue>`):
            N/A

    """

    __slots__: List[str] = ["key", "value"]

    ID = 0xc0de1bd9
    QUALNAME = "types.JsonObjectValue"

    def __init__(self, *, key: str, value: "raw.base.JSONValue") -> None:
        self.key = key
        self.value = value

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "JsonObjectValue":
        
        key = String.read(b)
        
        value = TLObject.read(b)
        
        return JsonObjectValue(key=key, value=value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.key))
        
        b.write(self.value.write())
        
        return b.getvalue()
