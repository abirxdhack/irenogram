


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputBotInlineResult = Union[raw.types.InputBotInlineResult, raw.types.InputBotInlineResultDocument, raw.types.InputBotInlineResultGame, raw.types.InputBotInlineResultPhoto]


class InputBotInlineResult:
    """Telegram API base type.

    Constructors:
        This base type has 4 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputBotInlineResult
            InputBotInlineResultDocument
            InputBotInlineResultGame
            InputBotInlineResultPhoto
    """

    QUALNAME = "pyrogram.raw.base.InputBotInlineResult"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/input-bot-inline-result")
