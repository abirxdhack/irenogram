


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ChannelParticipant = Union[raw.types.ChannelParticipant, raw.types.ChannelParticipantAdmin, raw.types.ChannelParticipantBanned, raw.types.ChannelParticipantCreator, raw.types.ChannelParticipantLeft, raw.types.ChannelParticipantSelf]


class ChannelParticipant:
    """Telegram API base type.

    Constructors:
        This base type has 6 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ChannelParticipant
            ChannelParticipantAdmin
            ChannelParticipantBanned
            ChannelParticipantCreator
            ChannelParticipantLeft
            ChannelParticipantSelf
    """

    QUALNAME = "pyrogram.raw.base.ChannelParticipant"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/channel-participant")
