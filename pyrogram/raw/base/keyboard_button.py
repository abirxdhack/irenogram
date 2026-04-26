


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

KeyboardButton = Union[raw.types.InputKeyboardButtonRequestPeer, raw.types.InputKeyboardButtonUrlAuth, raw.types.InputKeyboardButtonUserProfile, raw.types.KeyboardButton, raw.types.KeyboardButtonBuy, raw.types.KeyboardButtonCallback, raw.types.KeyboardButtonCopy, raw.types.KeyboardButtonGame, raw.types.KeyboardButtonRequestGeoLocation, raw.types.KeyboardButtonRequestPeer, raw.types.KeyboardButtonRequestPhone, raw.types.KeyboardButtonRequestPoll, raw.types.KeyboardButtonSimpleWebView, raw.types.KeyboardButtonSwitchInline, raw.types.KeyboardButtonUrl, raw.types.KeyboardButtonUrlAuth, raw.types.KeyboardButtonUserProfile, raw.types.KeyboardButtonWebView]


class KeyboardButton:
    """Telegram API base type.

    Constructors:
        This base type has 18 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputKeyboardButtonRequestPeer
            InputKeyboardButtonUrlAuth
            InputKeyboardButtonUserProfile
            KeyboardButton
            KeyboardButtonBuy
            KeyboardButtonCallback
            KeyboardButtonCopy
            KeyboardButtonGame
            KeyboardButtonRequestGeoLocation
            KeyboardButtonRequestPeer
            KeyboardButtonRequestPhone
            KeyboardButtonRequestPoll
            KeyboardButtonSimpleWebView
            KeyboardButtonSwitchInline
            KeyboardButtonUrl
            KeyboardButtonUrlAuth
            KeyboardButtonUserProfile
            KeyboardButtonWebView

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.GetRequestedWebViewButton
    """

    QUALNAME = "pyrogram.raw.base.KeyboardButton"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/keyboard-button")
