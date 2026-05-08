


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

AllStories = Union[raw.types.stories.AllStories, raw.types.stories.AllStoriesNotModified]


class AllStories:
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            stories.AllStories
            stories.AllStoriesNotModified

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.GetAllStories
    """

    QUALNAME = "pyrogram.raw.base.stories.AllStories"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/all-stories")
