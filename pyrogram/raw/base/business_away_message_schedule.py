


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

BusinessAwayMessageSchedule = Union[raw.types.BusinessAwayMessageScheduleAlways, raw.types.BusinessAwayMessageScheduleCustom, raw.types.BusinessAwayMessageScheduleOutsideWorkHours]


class BusinessAwayMessageSchedule:
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            BusinessAwayMessageScheduleAlways
            BusinessAwayMessageScheduleCustom
            BusinessAwayMessageScheduleOutsideWorkHours
    """

    QUALNAME = "pyrogram.raw.base.BusinessAwayMessageSchedule"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/business-away-message-schedule")
