
from pyrogram import raw

from ..object import Object


class PaidMessagesRefunded(Object):
    """Paid messages were refunded.

    Parameters:
        message_count (``int``):
            The number of refunded messages.

        star_count (``int``):
            The number of refunded Telegram Stars.
    """

    def __init__(
        self,
        *,
        message_count: int,
        star_count: int
    ):

        super().__init__()

        self.message_count = message_count
        self.star_count = star_count

    @staticmethod
    def _parse(
        action: "raw.types.MessageActionPaidMessagesRefunded"
    ) -> "PaidMessagesRefunded":
        return PaidMessagesRefunded(
            message_count=action.count,
            star_count=action.stars
        )
