
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SecureValueTypePersonalDetails(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SecureValueType`.

    Details:
        - Layer: ``224``
        - ID: ``9D2A81E3``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x9d2a81e3
    QUALNAME = "types.SecureValueTypePersonalDetails"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureValueTypePersonalDetails":
        
        return SecureValueTypePersonalDetails()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
