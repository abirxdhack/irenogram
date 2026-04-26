
from enum import auto

from .auto_name import AutoName


class SuggestedPostState(AutoName):
    """Suggested post state enumeration used in :obj:`~pyrogram.types.SuggestedPostInfo`."""

    PENDING = auto()
    """The post must be approved or declined."""

    APPROVED = auto()
    """The post was approved"""

    DECLINED = auto()
    """The post was declined"""
