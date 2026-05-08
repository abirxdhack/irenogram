


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

BotInlineResult = Union[raw.types.BotInlineMediaResult, raw.types.BotInlineResult]


class BotInlineResult:
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            BotInlineMediaResult
            BotInlineResult
    """

    QUALNAME = "pyrogram.raw.base.BotInlineResult"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/bot-inline-result")
