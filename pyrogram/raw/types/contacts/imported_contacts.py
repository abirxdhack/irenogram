
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ImportedContacts(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.contacts.ImportedContacts`.

    Details:
        - Layer: ``224``
        - ID: ``77D01C3B``

    Parameters:
        imported (List of :obj:`ImportedContact <pyrogram.raw.base.ImportedContact>`):
            N/A

        popular_invites (List of :obj:`PopularContact <pyrogram.raw.base.PopularContact>`):
            N/A

        retry_contacts (List of ``int`` ``64-bit``):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.ImportContacts
    """

    __slots__: List[str] = ["imported", "popular_invites", "retry_contacts", "users"]

    ID = 0x77d01c3b
    QUALNAME = "types.contacts.ImportedContacts"

    def __init__(self, *, imported: List["raw.base.ImportedContact"], popular_invites: List["raw.base.PopularContact"], retry_contacts: List[int], users: List["raw.base.User"]) -> None:
        self.imported = imported
        self.popular_invites = popular_invites
        self.retry_contacts = retry_contacts
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ImportedContacts":
        
        imported = TLObject.read(b)
        
        popular_invites = TLObject.read(b)
        
        retry_contacts = TLObject.read(b, Long)
        
        users = TLObject.read(b)
        
        return ImportedContacts(imported=imported, popular_invites=popular_invites, retry_contacts=retry_contacts, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.imported))
        
        b.write(Vector(self.popular_invites))
        
        b.write(Vector(self.retry_contacts, Long))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
