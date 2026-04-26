


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

BotMenuButton = Union[raw.types.BotMenuButton, raw.types.BotMenuButtonCommands, raw.types.BotMenuButtonDefault]


class BotMenuButton:
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            BotMenuButton
            BotMenuButtonCommands
            BotMenuButtonDefault

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.GetBotMenuButton
    """

    QUALNAME = "pyrogram.raw.base.BotMenuButton"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/bot-menu-button")
