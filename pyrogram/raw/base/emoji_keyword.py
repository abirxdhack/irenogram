


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

EmojiKeyword = Union[raw.types.EmojiKeyword, raw.types.EmojiKeywordDeleted]


class EmojiKeyword:
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            EmojiKeyword
            EmojiKeywordDeleted
    """

    QUALNAME = "pyrogram.raw.base.EmojiKeyword"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/emoji-keyword")
