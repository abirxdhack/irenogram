


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

Contacts = Union[raw.types.contacts.Contacts, raw.types.contacts.ContactsNotModified]


class Contacts:
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            contacts.Contacts
            contacts.ContactsNotModified

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.GetContacts
    """

    QUALNAME = "pyrogram.raw.base.contacts.Contacts"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/contacts")
