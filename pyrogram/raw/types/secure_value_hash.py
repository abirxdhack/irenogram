
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SecureValueHash(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SecureValueHash`.

    Details:
        - Layer: ``224``
        - ID: ``ED1ECDB0``

    Parameters:
        type (:obj:`SecureValueType <pyrogram.raw.base.SecureValueType>`):
            N/A

        hash (``bytes``):
            N/A

    """

    __slots__: List[str] = ["type", "hash"]

    ID = 0xed1ecdb0
    QUALNAME = "types.SecureValueHash"

    def __init__(self, *, type: "raw.base.SecureValueType", hash: bytes) -> None:
        self.type = type
        self.hash = hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureValueHash":
        
        type = TLObject.read(b)
        
        hash = Bytes.read(b)
        
        return SecureValueHash(type=type, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.type.write())
        
        b.write(Bytes(self.hash))
        
        return b.getvalue()
