
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DestroyAuthKey(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``D1435160``

    Parameters:
        No parameters required.

    Returns:
        :obj:`DestroyAuthKeyRes <pyrogram.raw.base.DestroyAuthKeyRes>`
    """

    __slots__: List[str] = []

    ID = 0xd1435160
    QUALNAME = "functions.DestroyAuthKey"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DestroyAuthKey":
        
        return DestroyAuthKey()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
