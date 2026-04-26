


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SavedDialogs = Union[raw.types.messages.SavedDialogs, raw.types.messages.SavedDialogsNotModified, raw.types.messages.SavedDialogsSlice]


class SavedDialogs:
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.SavedDialogs
            messages.SavedDialogsNotModified
            messages.SavedDialogsSlice

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSavedDialogs
            messages.GetPinnedSavedDialogs
            messages.GetSavedDialogsByID
    """

    QUALNAME = "pyrogram.raw.base.messages.SavedDialogs"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/saved-dialogs")
