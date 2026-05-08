


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PrivacyRule = Union[raw.types.PrivacyValueAllowAll, raw.types.PrivacyValueAllowBots, raw.types.PrivacyValueAllowChatParticipants, raw.types.PrivacyValueAllowCloseFriends, raw.types.PrivacyValueAllowContacts, raw.types.PrivacyValueAllowPremium, raw.types.PrivacyValueAllowUsers, raw.types.PrivacyValueDisallowAll, raw.types.PrivacyValueDisallowBots, raw.types.PrivacyValueDisallowChatParticipants, raw.types.PrivacyValueDisallowContacts, raw.types.PrivacyValueDisallowUsers]


class PrivacyRule:
    """Telegram API base type.

    Constructors:
        This base type has 12 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PrivacyValueAllowAll
            PrivacyValueAllowBots
            PrivacyValueAllowChatParticipants
            PrivacyValueAllowCloseFriends
            PrivacyValueAllowContacts
            PrivacyValueAllowPremium
            PrivacyValueAllowUsers
            PrivacyValueDisallowAll
            PrivacyValueDisallowBots
            PrivacyValueDisallowChatParticipants
            PrivacyValueDisallowContacts
            PrivacyValueDisallowUsers
    """

    QUALNAME = "pyrogram.raw.base.PrivacyRule"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/privacy-rule")
