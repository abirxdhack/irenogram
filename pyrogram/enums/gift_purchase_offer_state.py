
from enum import auto

from .auto_name import AutoName


class GiftPurchaseOfferState(AutoName):
    """Gift purchase offer state enumeration used in :obj:`~pyrogram.types.UpgradedGiftPurchaseOffer`."""

    PENDING = auto()
    """The offer must be accepted or rejected"""

    ACCEPTED = auto()
    """The offer was accepted"""

    REJECTED = auto()
    """The offer was rejected"""
