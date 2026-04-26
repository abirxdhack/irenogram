
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EncryptedChatEmpty(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.EncryptedChat`.

    Details:
        - Layer: ``224``
        - ID: ``AB7EC0A0``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.RequestEncryption
            messages.AcceptEncryption
    """

    __slots__: List[str] = ["id"]

    ID = 0xab7ec0a0
    QUALNAME = "types.EncryptedChatEmpty"

    def __init__(self, *, id: int) -> None:
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EncryptedChatEmpty":
        
        id = Int.read(b)
        
        return EncryptedChatEmpty(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.id))
        
        return b.getvalue()
