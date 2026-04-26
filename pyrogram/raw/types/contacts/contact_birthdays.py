
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ContactBirthdays(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.contacts.ContactBirthdays`.

    Details:
        - Layer: ``224``
        - ID: ``114FF30D``

    Parameters:
        contacts (List of :obj:`ContactBirthday <pyrogram.raw.base.ContactBirthday>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.GetBirthdays
    """

    __slots__: List[str] = ["contacts", "users"]

    ID = 0x114ff30d
    QUALNAME = "types.contacts.ContactBirthdays"

    def __init__(self, *, contacts: List["raw.base.ContactBirthday"], users: List["raw.base.User"]) -> None:
        self.contacts = contacts
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ContactBirthdays":
        
        contacts = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return ContactBirthdays(contacts=contacts, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.contacts))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
