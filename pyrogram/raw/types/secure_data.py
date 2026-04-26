
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SecureData(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SecureData`.

    Details:
        - Layer: ``224``
        - ID: ``8AEABEC3``

    Parameters:
        data (``bytes``):
            N/A

        data_hash (``bytes``):
            N/A

        secret (``bytes``):
            N/A

    """

    __slots__: List[str] = ["data", "data_hash", "secret"]

    ID = 0x8aeabec3
    QUALNAME = "types.SecureData"

    def __init__(self, *, data: bytes, data_hash: bytes, secret: bytes) -> None:
        self.data = data
        self.data_hash = data_hash
        self.secret = secret

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureData":
        
        data = Bytes.read(b)
        
        data_hash = Bytes.read(b)
        
        secret = Bytes.read(b)
        
        return SecureData(data=data, data_hash=data_hash, secret=secret)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Bytes(self.data))
        
        b.write(Bytes(self.data_hash))
        
        b.write(Bytes(self.secret))
        
        return b.getvalue()
