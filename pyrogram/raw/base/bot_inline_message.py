


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

BotInlineMessage = Union[raw.types.BotInlineMessageMediaAuto, raw.types.BotInlineMessageMediaContact, raw.types.BotInlineMessageMediaGeo, raw.types.BotInlineMessageMediaInvoice, raw.types.BotInlineMessageMediaVenue, raw.types.BotInlineMessageMediaWebPage, raw.types.BotInlineMessageText]


class BotInlineMessage:
    """Telegram API base type.

    Constructors:
        This base type has 7 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            BotInlineMessageMediaAuto
            BotInlineMessageMediaContact
            BotInlineMessageMediaGeo
            BotInlineMessageMediaInvoice
            BotInlineMessageMediaVenue
            BotInlineMessageMediaWebPage
            BotInlineMessageText
    """

    QUALNAME = "pyrogram.raw.base.BotInlineMessage"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/bot-inline-message")
