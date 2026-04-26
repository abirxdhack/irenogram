


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PaymentForm = Union[raw.types.payments.PaymentForm, raw.types.payments.PaymentFormStarGift, raw.types.payments.PaymentFormStars]


class PaymentForm:
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            payments.PaymentForm
            payments.PaymentFormStarGift
            payments.PaymentFormStars

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetPaymentForm
    """

    QUALNAME = "pyrogram.raw.base.payments.PaymentForm"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/payment-form")
