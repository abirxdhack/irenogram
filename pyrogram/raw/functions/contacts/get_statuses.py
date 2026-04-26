
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetStatuses(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``C4A353EE``

    Parameters:
        No parameters required.

    Returns:
        List of :obj:`ContactStatus <pyrogram.raw.base.ContactStatus>`
    """

    __slots__: List[str] = []

    ID = 0xc4a353ee
    QUALNAME = "functions.contacts.GetStatuses"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStatuses":
        
        return GetStatuses()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
