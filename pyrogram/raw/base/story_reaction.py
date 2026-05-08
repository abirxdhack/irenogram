


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

StoryReaction = Union[raw.types.StoryReaction, raw.types.StoryReactionPublicForward, raw.types.StoryReactionPublicRepost]


class StoryReaction:
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            StoryReaction
            StoryReactionPublicForward
            StoryReactionPublicRepost
    """

    QUALNAME = "pyrogram.raw.base.StoryReaction"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/story-reaction")
