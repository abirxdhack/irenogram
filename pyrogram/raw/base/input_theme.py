


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputTheme = Union[raw.types.InputTheme, raw.types.InputThemeSlug]


class InputTheme:
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputTheme
            InputThemeSlug
    """

    QUALNAME = "pyrogram.raw.base.InputTheme"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/input-theme")
