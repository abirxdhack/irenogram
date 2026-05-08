
from enum import auto

from .auto_name import AutoName

class GiftForResaleOrder(AutoName):
    """Describes order in which upgraded gifts for resale will be sorted. Used in :meth:`~pyrogram.Client.search_gifts_for_resale`."""

    PRICE = auto()
    "The gifts will be sorted by their price from the lowest to the highest"

    CHANGE_DATE = auto()
    "The gifts will be sorted by the last date when their price was changed from the newest to the oldest"

    NUMBER = auto()
    "The gifts will be sorted by their number from the smallest to the largest"
