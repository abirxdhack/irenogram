
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SecureValueErrorData(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SecureValueError`.

    Details:
        - Layer: ``224``
        - ID: ``E8A40BD9``

    Parameters:
        type (:obj:`SecureValueType <pyrogram.raw.base.SecureValueType>`):
            N/A

        data_hash (``bytes``):
            N/A

        field (``str``):
            N/A

        text (``str``):
            N/A

    """

    __slots__: List[str] = ["type", "data_hash", "field", "text"]

    ID = 0xe8a40bd9
    QUALNAME = "types.SecureValueErrorData"

    def __init__(self, *, type: "raw.base.SecureValueType", data_hash: bytes, field: str, text: str) -> None:
        self.type = type
        self.data_hash = data_hash
        self.field = field
        self.text = text

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureValueErrorData":
        
        type = TLObject.read(b)
        
        data_hash = Bytes.read(b)
        
        field = String.read(b)
        
        text = String.read(b)
        
        return SecureValueErrorData(type=type, data_hash=data_hash, field=field, text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.type.write())
        
        b.write(Bytes(self.data_hash))
        
        b.write(String(self.field))
        
        b.write(String(self.text))
        
        return b.getvalue()
