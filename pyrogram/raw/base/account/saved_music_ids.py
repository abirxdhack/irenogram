


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SavedMusicIds = Union[raw.types.account.SavedMusicIds, raw.types.account.SavedMusicIdsNotModified]


class SavedMusicIds:
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            account.SavedMusicIds
            account.SavedMusicIdsNotModified

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetSavedMusicIds
    """

    QUALNAME = "pyrogram.raw.base.account.SavedMusicIds"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/saved-music-ids")
