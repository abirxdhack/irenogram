


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputPaymentCredentials = Union[raw.types.InputPaymentCredentials, raw.types.InputPaymentCredentialsApplePay, raw.types.InputPaymentCredentialsGooglePay, raw.types.InputPaymentCredentialsSaved]


class InputPaymentCredentials:
    """Telegram API base type.

    Constructors:
        This base type has 4 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputPaymentCredentials
            InputPaymentCredentialsApplePay
            InputPaymentCredentialsGooglePay
            InputPaymentCredentialsSaved
    """

    QUALNAME = "pyrogram.raw.base.InputPaymentCredentials"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/input-payment-credentials")
