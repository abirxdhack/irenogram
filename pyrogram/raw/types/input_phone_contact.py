
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputPhoneContact(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputContact`.

    Details:
        - Layer: ``224``
        - ID: ``6A1DC4BE``

    Parameters:
        client_id (``int`` ``64-bit``):
            N/A

        phone (``str``):
            N/A

        first_name (``str``):
            N/A

        last_name (``str``):
            N/A

        note (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["client_id", "phone", "first_name", "last_name", "note"]

    ID = 0x6a1dc4be
    QUALNAME = "types.InputPhoneContact"

    def __init__(self, *, client_id: int, phone: str, first_name: str, last_name: str, note: "raw.base.TextWithEntities" = None) -> None:
        self.client_id = client_id
        self.phone = phone
        self.first_name = first_name
        self.last_name = last_name
        self.note = note

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPhoneContact":
        
        flags = Int.read(b)
        
        client_id = Long.read(b)
        
        phone = String.read(b)
        
        first_name = String.read(b)
        
        last_name = String.read(b)
        
        note = TLObject.read(b) if flags & (1 << 0) else None
        
        return InputPhoneContact(client_id=client_id, phone=phone, first_name=first_name, last_name=last_name, note=note)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.note is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.client_id))
        
        b.write(String(self.phone))
        
        b.write(String(self.first_name))
        
        b.write(String(self.last_name))
        
        if self.note is not None:
            b.write(self.note.write())
        
        return b.getvalue()
