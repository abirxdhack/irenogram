


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PrivacyKey = Union[raw.types.PrivacyKeyAbout, raw.types.PrivacyKeyAddedByPhone, raw.types.PrivacyKeyBirthday, raw.types.PrivacyKeyChatInvite, raw.types.PrivacyKeyForwards, raw.types.PrivacyKeyNoPaidMessages, raw.types.PrivacyKeyPhoneCall, raw.types.PrivacyKeyPhoneNumber, raw.types.PrivacyKeyPhoneP2P, raw.types.PrivacyKeyProfilePhoto, raw.types.PrivacyKeySavedMusic, raw.types.PrivacyKeyStarGiftsAutoSave, raw.types.PrivacyKeyStatusTimestamp, raw.types.PrivacyKeyVoiceMessages]


class PrivacyKey:
    """Telegram API base type.

    Constructors:
        This base type has 14 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PrivacyKeyAbout
            PrivacyKeyAddedByPhone
            PrivacyKeyBirthday
            PrivacyKeyChatInvite
            PrivacyKeyForwards
            PrivacyKeyNoPaidMessages
            PrivacyKeyPhoneCall
            PrivacyKeyPhoneNumber
            PrivacyKeyPhoneP2P
            PrivacyKeyProfilePhoto
            PrivacyKeySavedMusic
            PrivacyKeyStarGiftsAutoSave
            PrivacyKeyStatusTimestamp
            PrivacyKeyVoiceMessages
    """

    QUALNAME = "pyrogram.raw.base.PrivacyKey"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/privacy-key")
