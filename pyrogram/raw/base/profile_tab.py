


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ProfileTab = Union[raw.types.ProfileTabFiles, raw.types.ProfileTabGifs, raw.types.ProfileTabGifts, raw.types.ProfileTabLinks, raw.types.ProfileTabMedia, raw.types.ProfileTabMusic, raw.types.ProfileTabPosts, raw.types.ProfileTabVoice]


class ProfileTab:
    """Telegram API base type.

    Constructors:
        This base type has 8 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ProfileTabFiles
            ProfileTabGifs
            ProfileTabGifts
            ProfileTabLinks
            ProfileTabMedia
            ProfileTabMusic
            ProfileTabPosts
            ProfileTabVoice
    """

    QUALNAME = "pyrogram.raw.base.ProfileTab"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/profile-tab")
