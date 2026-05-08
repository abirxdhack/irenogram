


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

CountriesList = Union[raw.types.help.CountriesList, raw.types.help.CountriesListNotModified]


class CountriesList:
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            help.CountriesList
            help.CountriesListNotModified

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetCountriesList
    """

    QUALNAME = "pyrogram.raw.base.help.CountriesList"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/countries-list")
