


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ChatInvite = Union[raw.types.ChatInvite, raw.types.ChatInviteAlready, raw.types.ChatInvitePeek]


class ChatInvite:
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ChatInvite
            ChatInviteAlready
            ChatInvitePeek

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.CheckChatInvite
    """

    QUALNAME = "pyrogram.raw.base.ChatInvite"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/chat-invite")
