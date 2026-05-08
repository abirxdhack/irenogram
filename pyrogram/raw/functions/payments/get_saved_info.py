
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetSavedInfo(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``227D824B``

    Parameters:
        No parameters required.

    Returns:
        :obj:`payments.SavedInfo <pyrogram.raw.base.payments.SavedInfo>`
    """

    __slots__: List[str] = []

    ID = 0x227d824b
    QUALNAME = "functions.payments.GetSavedInfo"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSavedInfo":
        
        return GetSavedInfo()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
