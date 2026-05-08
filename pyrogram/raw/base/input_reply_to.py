


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputReplyTo = Union[raw.types.InputReplyToMessage, raw.types.InputReplyToMonoForum, raw.types.InputReplyToStory]


class InputReplyTo:
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputReplyToMessage
            InputReplyToMonoForum
            InputReplyToStory
    """

    QUALNAME = "pyrogram.raw.base.InputReplyTo"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/input-reply-to")
