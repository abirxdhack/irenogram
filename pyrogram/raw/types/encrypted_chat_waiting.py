
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EncryptedChatWaiting(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.EncryptedChat`.

    Details:
        - Layer: ``224``
        - ID: ``66B25953``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

        access_hash (``int`` ``64-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        admin_id (``int`` ``64-bit``):
            N/A

        participant_id (``int`` ``64-bit``):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.RequestEncryption
            messages.AcceptEncryption
    """

    __slots__: List[str] = ["id", "access_hash", "date", "admin_id", "participant_id"]

    ID = 0x66b25953
    QUALNAME = "types.EncryptedChatWaiting"

    def __init__(self, *, id: int, access_hash: int, date: int, admin_id: int, participant_id: int) -> None:
        self.id = id
        self.access_hash = access_hash
        self.date = date
        self.admin_id = admin_id
        self.participant_id = participant_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EncryptedChatWaiting":
        
        id = Int.read(b)
        
        access_hash = Long.read(b)
        
        date = Int.read(b)
        
        admin_id = Long.read(b)
        
        participant_id = Long.read(b)
        
        return EncryptedChatWaiting(id=id, access_hash=access_hash, date=date, admin_id=admin_id, participant_id=participant_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(Int(self.date))
        
        b.write(Long(self.admin_id))
        
        b.write(Long(self.participant_id))
        
        return b.getvalue()
