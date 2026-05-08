
from enum import auto

from .auto_name import AutoName


class PaymentFormType(AutoName):
    """Describes type of payment form."""

    REGULAR = auto()
    "The payment form is for a regular payment"

    STARS = auto()
    "The payment form is for a payment in Telegram Stars"

    STAR_SUBSCRIPTION = auto()
    "The payment form is for a payment in Telegram Stars for subscription"
