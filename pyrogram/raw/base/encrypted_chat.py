


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

EncryptedChat = Union[raw.types.EncryptedChat, raw.types.EncryptedChatDiscarded, raw.types.EncryptedChatEmpty, raw.types.EncryptedChatRequested, raw.types.EncryptedChatWaiting]


class EncryptedChat:
    """Telegram API base type.

    Constructors:
        This base type has 5 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            EncryptedChat
            EncryptedChatDiscarded
            EncryptedChatEmpty
            EncryptedChatRequested
            EncryptedChatWaiting

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.RequestEncryption
            messages.AcceptEncryption
    """

    QUALNAME = "pyrogram.raw.base.EncryptedChat"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/encrypted-chat")
