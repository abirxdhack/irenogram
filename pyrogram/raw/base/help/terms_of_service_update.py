


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

TermsOfServiceUpdate = Union[raw.types.help.TermsOfServiceUpdate, raw.types.help.TermsOfServiceUpdateEmpty]


class TermsOfServiceUpdate:
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            help.TermsOfServiceUpdate
            help.TermsOfServiceUpdateEmpty

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetTermsOfServiceUpdate
    """

    QUALNAME = "pyrogram.raw.base.help.TermsOfServiceUpdate"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/terms-of-service-update")
