
from typing import List, Union

from pyrogram import raw
from pyrogram import types
from ..object import Object

class PaidMessagePriceChanged(Object):
    """A PaidMessagePriceChanged.


    Parameters:
        stars_amount (``int``):
            Amount of stars.

        extended_media (List of :obj:`~pyrogram.types.Animation` | :obj:`~pyrogram.types.ExtendedMediaPreview` | :obj:`~pyrogram.types.Photo` | :obj:`~pyrogram.types.Video`, *optional*):
            Extended media.
    """
    def __init__(
            self,
            *,
            stars_amount: int,
    ):
        super().__init__()

        self.stars_amount = stars_amount

    @staticmethod
    def _parse(action: "raw.types.MessageActionPaidMessagesPrice") -> "PaidMessagePriceChanged":
        return PaidMessagePriceChanged(
            stars_amount=action.stars
        )
