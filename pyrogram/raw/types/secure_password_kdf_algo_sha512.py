
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SecurePasswordKdfAlgoSHA512(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SecurePasswordKdfAlgo`.

    Details:
        - Layer: ``224``
        - ID: ``86471D92``

    Parameters:
        salt (``bytes``):
            N/A

    """

    __slots__: List[str] = ["salt"]

    ID = 0x86471d92
    QUALNAME = "types.SecurePasswordKdfAlgoSHA512"

    def __init__(self, *, salt: bytes) -> None:
        self.salt = salt

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecurePasswordKdfAlgoSHA512":
        
        salt = Bytes.read(b)
        
        return SecurePasswordKdfAlgoSHA512(salt=salt)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Bytes(self.salt))
        
        return b.getvalue()
