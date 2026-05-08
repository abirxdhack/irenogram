
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class AddContact(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``D9BA2E54``

    Parameters:
        id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        first_name (``str``):
            N/A

        last_name (``str``):
            N/A

        phone (``str``):
            N/A

        add_phone_privacy_exception (``bool``, *optional*):
            N/A

        note (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["id", "first_name", "last_name", "phone", "add_phone_privacy_exception", "note"]

    ID = 0xd9ba2e54
    QUALNAME = "functions.contacts.AddContact"

    def __init__(self, *, id: "raw.base.InputUser", first_name: str, last_name: str, phone: str, add_phone_privacy_exception: Optional[bool] = None, note: "raw.base.TextWithEntities" = None) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.add_phone_privacy_exception = add_phone_privacy_exception
        self.note = note

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AddContact":
        
        flags = Int.read(b)
        
        add_phone_privacy_exception = True if flags & (1 << 0) else False
        id = TLObject.read(b)
        
        first_name = String.read(b)
        
        last_name = String.read(b)
        
        phone = String.read(b)
        
        note = TLObject.read(b) if flags & (1 << 1) else None
        
        return AddContact(id=id, first_name=first_name, last_name=last_name, phone=phone, add_phone_privacy_exception=add_phone_privacy_exception, note=note)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.add_phone_privacy_exception else 0
        flags |= (1 << 1) if self.note is not None else 0
        b.write(Int(flags))
        
        b.write(self.id.write())
        
        b.write(String(self.first_name))
        
        b.write(String(self.last_name))
        
        b.write(String(self.phone))
        
        if self.note is not None:
            b.write(self.note.write())
        
        return b.getvalue()
