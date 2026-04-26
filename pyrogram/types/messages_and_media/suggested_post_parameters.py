
from datetime import datetime
from typing import Optional

from pyrogram import raw, types, utils

from ..object import Object


class SuggestedPostParameters(Object):
    """Contains parameters of a post that is being suggested.

    Parameters:
        price (:obj:`~pyrogram.types.SuggestedPostPrice`, *optional*):
            Proposed price for the post. If the field is omitted, then the post is unpaid.

        send_date (:py:obj:`~datetime.datetime`, *optional*):
            Proposed send date of the post.
            If specified, then the date must be between 300 second and 2678400 seconds (30 days) in the future.
            If the field is omitted, then the post can be published at any time within 30 days at the sole discretion of the user who approves it.
    """
    def __init__(
        self, *,
        price: Optional["types.SuggestedPostPrice"] = None,
        send_date: Optional[datetime] = None
    ):
        super().__init__()

        self.price = price
        self.send_date = send_date

    def write(self) -> "raw.types.SuggestedPost":
        return raw.types.SuggestedPost(
            price=self.price.write() if self.price else None,
            schedule_date=utils.datetime_to_timestamp(self.send_date)
        )
