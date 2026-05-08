


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

Stories = Union[raw.types.stories.Stories]


class Stories:
    """Telegram API base type.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            stories.Stories

    Functions:
        This object can be returned by 4 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.GetPinnedStories
            stories.GetStoriesArchive
            stories.GetStoriesByID
            stories.GetAlbumStories
    """

    QUALNAME = "pyrogram.raw.base.stories.Stories"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/stories")
