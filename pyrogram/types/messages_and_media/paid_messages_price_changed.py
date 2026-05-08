
from pyrogram import raw

from ..object import Object


class PaidMessagesPriceChanged(Object):
    """A price for paid messages was changed in the supergroup chat.

    Parameters:
        paid_message_star_count (``int``):
            The new number of Telegram Stars that must be paid by non-administrator users of the supergroup chat for each sent message.
    """

    def __init__(
        self,
        *,
        paid_message_star_count: int
    ):

        super().__init__()

        self.paid_message_star_count = paid_message_star_count

    @staticmethod
    def _parse(
        action: "raw.types.MessageActionPaidMessagesPrice"
    ) -> "PaidMessagesPriceChanged":
        return PaidMessagesPriceChanged(
            paid_message_star_count=action.stars
        )
