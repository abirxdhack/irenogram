
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SecurePasswordKdfAlgo`.

    Details:
        - Layer: ``224``
        - ID: ``BBF2DDA0``

    Parameters:
        salt (``bytes``):
            N/A

    """

    __slots__: List[str] = ["salt"]

    ID = 0xbbf2dda0
    QUALNAME = "types.SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000"

    def __init__(self, *, salt: bytes) -> None:
        self.salt = salt

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000":
        
        salt = Bytes.read(b)
        
        return SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000(salt=salt)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Bytes(self.salt))
        
        return b.getvalue()
