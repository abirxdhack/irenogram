


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

RequirementToContact = Union[raw.types.RequirementToContactEmpty, raw.types.RequirementToContactPaidMessages, raw.types.RequirementToContactPremium]


class RequirementToContact:
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            RequirementToContactEmpty
            RequirementToContactPaidMessages
            RequirementToContactPremium

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            users.GetRequirementsToContact
    """

    QUALNAME = "pyrogram.raw.base.RequirementToContact"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/requirement-to-contact")
