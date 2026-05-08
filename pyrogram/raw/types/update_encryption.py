
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateEncryption(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``B4A2E88D``

    Parameters:
        chat (:obj:`EncryptedChat <pyrogram.raw.base.EncryptedChat>`):
            N/A

        date (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["chat", "date"]

    ID = 0xb4a2e88d
    QUALNAME = "types.UpdateEncryption"

    def __init__(self, *, chat: "raw.base.EncryptedChat", date: int) -> None:
        self.chat = chat
        self.date = date

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateEncryption":
        
        chat = TLObject.read(b)
        
        date = Int.read(b)
        
        return UpdateEncryption(chat=chat, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.chat.write())
        
        b.write(Int(self.date))
        
        return b.getvalue()
