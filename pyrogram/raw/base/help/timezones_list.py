


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

TimezonesList = Union[raw.types.help.TimezonesList, raw.types.help.TimezonesListNotModified]


class TimezonesList:
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            help.TimezonesList
            help.TimezonesListNotModified

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetTimezonesList
    """

    QUALNAME = "pyrogram.raw.base.help.TimezonesList"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/timezones-list")
