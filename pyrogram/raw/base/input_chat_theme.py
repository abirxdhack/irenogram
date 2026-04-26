


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputChatTheme = Union[raw.types.InputChatTheme, raw.types.InputChatThemeEmpty, raw.types.InputChatThemeUniqueGift]


class InputChatTheme:
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputChatTheme
            InputChatThemeEmpty
            InputChatThemeUniqueGift
    """

    QUALNAME = "pyrogram.raw.base.InputChatTheme"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/input-chat-theme")
