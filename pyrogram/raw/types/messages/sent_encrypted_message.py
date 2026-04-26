
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SentEncryptedMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.SentEncryptedMessage`.

    Details:
        - Layer: ``224``
        - ID: ``560F8935``

    Parameters:
        date (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.SendEncrypted
            messages.SendEncryptedFile
            messages.SendEncryptedService
    """

    __slots__: List[str] = ["date"]

    ID = 0x560f8935
    QUALNAME = "types.messages.SentEncryptedMessage"

    def __init__(self, *, date: int) -> None:
        self.date = date

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentEncryptedMessage":
        
        date = Int.read(b)
        
        return SentEncryptedMessage(date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.date))
        
        return b.getvalue()
