
from enum import auto

from .auto_name import AutoName


class SuggestedPostRefundReason(AutoName):
    """Suggested post refund reason enumeration used in :obj:`~pyrogram.types.SuggestedPostRefunded`."""

    POST_DELETED = auto()
    """The post was deleted within 24 hours of being posted or removed from scheduled messages without being posted"""

    PAYMENT_REFUNDED = auto()
    """The post was refunded, because the payment for the post was refunded."""
