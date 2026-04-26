


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputStorePaymentPurpose = Union[raw.types.InputStorePaymentAuthCode, raw.types.InputStorePaymentGiftPremium, raw.types.InputStorePaymentPremiumGiftCode, raw.types.InputStorePaymentPremiumGiveaway, raw.types.InputStorePaymentPremiumSubscription, raw.types.InputStorePaymentStarsGift, raw.types.InputStorePaymentStarsGiveaway, raw.types.InputStorePaymentStarsTopup]


class InputStorePaymentPurpose:
    """Telegram API base type.

    Constructors:
        This base type has 8 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputStorePaymentAuthCode
            InputStorePaymentGiftPremium
            InputStorePaymentPremiumGiftCode
            InputStorePaymentPremiumGiveaway
            InputStorePaymentPremiumSubscription
            InputStorePaymentStarsGift
            InputStorePaymentStarsGiveaway
            InputStorePaymentStarsTopup
    """

    QUALNAME = "pyrogram.raw.base.InputStorePaymentPurpose"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/input-store-payment-purpose")
