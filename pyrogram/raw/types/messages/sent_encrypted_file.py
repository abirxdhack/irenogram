
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SentEncryptedFile(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.SentEncryptedMessage`.

    Details:
        - Layer: ``224``
        - ID: ``9493FF32``

    Parameters:
        date (``int`` ``32-bit``):
            N/A

        file (:obj:`EncryptedFile <pyrogram.raw.base.EncryptedFile>`):
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

    __slots__: List[str] = ["date", "file"]

    ID = 0x9493ff32
    QUALNAME = "types.messages.SentEncryptedFile"

    def __init__(self, *, date: int, file: "raw.base.EncryptedFile") -> None:
        self.date = date
        self.file = file

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentEncryptedFile":
        
        date = Int.read(b)
        
        file = TLObject.read(b)
        
        return SentEncryptedFile(date=date, file=file)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.date))
        
        b.write(self.file.write())
        
        return b.getvalue()
