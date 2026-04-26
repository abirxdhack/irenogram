
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ContactBirthday(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ContactBirthday`.

    Details:
        - Layer: ``224``
        - ID: ``1D998733``

    Parameters:
        contact_id (``int`` ``64-bit``):
            N/A

        birthday (:obj:`Birthday <pyrogram.raw.base.Birthday>`):
            N/A

    """

    __slots__: List[str] = ["contact_id", "birthday"]

    ID = 0x1d998733
    QUALNAME = "types.ContactBirthday"

    def __init__(self, *, contact_id: int, birthday: "raw.base.Birthday") -> None:
        self.contact_id = contact_id
        self.birthday = birthday

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ContactBirthday":
        
        contact_id = Long.read(b)
        
        birthday = TLObject.read(b)
        
        return ContactBirthday(contact_id=contact_id, birthday=birthday)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.contact_id))
        
        b.write(self.birthday.write())
        
        return b.getvalue()
