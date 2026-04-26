
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SecureValueTypeInternalPassport(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SecureValueType`.

    Details:
        - Layer: ``224``
        - ID: ``99A48F23``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x99a48f23
    QUALNAME = "types.SecureValueTypeInternalPassport"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureValueTypeInternalPassport":
        
        return SecureValueTypeInternalPassport()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
