
from enum import auto

from .auto_name import AutoName


class GiftType(AutoName):
    """Gift type enumeration used in :obj:`~pyrogram.types.Gift`."""

    REGULAR = auto()
    "Gift is a regular gift"

    UPGRADED = auto()
    "Gift is an upgraded gift"
