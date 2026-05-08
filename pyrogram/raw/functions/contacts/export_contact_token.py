
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ExportContactToken(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``F8654027``

    Parameters:
        No parameters required.

    Returns:
        :obj:`ExportedContactToken <pyrogram.raw.base.ExportedContactToken>`
    """

    __slots__: List[str] = []

    ID = 0xf8654027
    QUALNAME = "functions.contacts.ExportContactToken"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportContactToken":
        
        return ExportContactToken()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
