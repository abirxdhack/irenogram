


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SavedGifs = Union[raw.types.messages.SavedGifs, raw.types.messages.SavedGifsNotModified]


class SavedGifs:
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.SavedGifs
            messages.SavedGifsNotModified

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSavedGifs
    """

    QUALNAME = "pyrogram.raw.base.messages.SavedGifs"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/saved-gifs")
