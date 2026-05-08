


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ChannelParticipantsFilter = Union[raw.types.ChannelParticipantsAdmins, raw.types.ChannelParticipantsBanned, raw.types.ChannelParticipantsBots, raw.types.ChannelParticipantsContacts, raw.types.ChannelParticipantsKicked, raw.types.ChannelParticipantsMentions, raw.types.ChannelParticipantsRecent, raw.types.ChannelParticipantsSearch]


class ChannelParticipantsFilter:
    """Telegram API base type.

    Constructors:
        This base type has 8 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ChannelParticipantsAdmins
            ChannelParticipantsBanned
            ChannelParticipantsBots
            ChannelParticipantsContacts
            ChannelParticipantsKicked
            ChannelParticipantsMentions
            ChannelParticipantsRecent
            ChannelParticipantsSearch
    """

    QUALNAME = "pyrogram.raw.base.ChannelParticipantsFilter"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/channel-participants-filter")
