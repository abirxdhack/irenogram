


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

StoryAlbum = Union[raw.types.StoryAlbum]


class StoryAlbum:
    """Telegram API base type.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            StoryAlbum

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.CreateAlbum
            stories.UpdateAlbum
    """

    QUALNAME = "pyrogram.raw.base.StoryAlbum"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/story-album")
