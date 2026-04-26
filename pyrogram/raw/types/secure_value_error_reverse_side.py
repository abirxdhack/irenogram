
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SecureValueErrorReverseSide(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SecureValueError`.

    Details:
        - Layer: ``224``
        - ID: ``868A2AA5``

    Parameters:
        type (:obj:`SecureValueType <pyrogram.raw.base.SecureValueType>`):
            N/A

        file_hash (``bytes``):
            N/A

        text (``str``):
            N/A

    """

    __slots__: List[str] = ["type", "file_hash", "text"]

    ID = 0x868a2aa5
    QUALNAME = "types.SecureValueErrorReverseSide"

    def __init__(self, *, type: "raw.base.SecureValueType", file_hash: bytes, text: str) -> None:
        self.type = type
        self.file_hash = file_hash
        self.text = text

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureValueErrorReverseSide":
        
        type = TLObject.read(b)
        
        file_hash = Bytes.read(b)
        
        text = String.read(b)
        
        return SecureValueErrorReverseSide(type=type, file_hash=file_hash, text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.type.write())
        
        b.write(Bytes(self.file_hash))
        
        b.write(String(self.text))
        
        return b.getvalue()
