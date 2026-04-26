


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

EmojiGroup = Union[raw.types.EmojiGroup, raw.types.EmojiGroupGreeting, raw.types.EmojiGroupPremium]


class EmojiGroup:
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            EmojiGroup
            EmojiGroupGreeting
            EmojiGroupPremium
    """

    QUALNAME = "pyrogram.raw.base.EmojiGroup"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/emoji-group")
