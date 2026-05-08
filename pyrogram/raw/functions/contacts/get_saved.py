
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetSaved(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``82F1E39F``

    Parameters:
        No parameters required.

    Returns:
        List of :obj:`SavedContact <pyrogram.raw.base.SavedContact>`
    """

    __slots__: List[str] = []

    ID = 0x82f1e39f
    QUALNAME = "functions.contacts.GetSaved"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSaved":
        
        return GetSaved()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
