


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

BaseTheme = Union[raw.types.BaseThemeArctic, raw.types.BaseThemeClassic, raw.types.BaseThemeDay, raw.types.BaseThemeNight, raw.types.BaseThemeTinted]


class BaseTheme:
    """Telegram API base type.

    Constructors:
        This base type has 5 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            BaseThemeArctic
            BaseThemeClassic
            BaseThemeDay
            BaseThemeNight
            BaseThemeTinted
    """

    QUALNAME = "pyrogram.raw.base.BaseTheme"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/base-theme")
