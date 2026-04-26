


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

TopPeerCategory = Union[raw.types.TopPeerCategoryBotsApp, raw.types.TopPeerCategoryBotsInline, raw.types.TopPeerCategoryBotsPM, raw.types.TopPeerCategoryChannels, raw.types.TopPeerCategoryCorrespondents, raw.types.TopPeerCategoryForwardChats, raw.types.TopPeerCategoryForwardUsers, raw.types.TopPeerCategoryGroups, raw.types.TopPeerCategoryPhoneCalls]


class TopPeerCategory:
    """Telegram API base type.

    Constructors:
        This base type has 9 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            TopPeerCategoryBotsApp
            TopPeerCategoryBotsInline
            TopPeerCategoryBotsPM
            TopPeerCategoryChannels
            TopPeerCategoryCorrespondents
            TopPeerCategoryForwardChats
            TopPeerCategoryForwardUsers
            TopPeerCategoryGroups
            TopPeerCategoryPhoneCalls
    """

    QUALNAME = "pyrogram.raw.base.TopPeerCategory"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/top-peer-category")
