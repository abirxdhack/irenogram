


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PrepaidGiveaway = Union[raw.types.PrepaidGiveaway, raw.types.PrepaidStarsGiveaway]


class PrepaidGiveaway:
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PrepaidGiveaway
            PrepaidStarsGiveaway
    """

    QUALNAME = "pyrogram.raw.base.PrepaidGiveaway"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/prepaid-giveaway")
