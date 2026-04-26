
from pyrogram import raw

from ..object import Object


class DirectMessagePriceChanged(Object):
    """A price for direct messages was changed in the channel chat.

    Parameters:
        is_enabled (``bool``):
            True, if direct messages group was enabled for the channel, False otherwise

        paid_message_star_count (``int``):
            The new number of Telegram Stars that must be paid by non-administrator users of the channel chat
            for each message sent to the direct messages group.
            0 if the direct messages group was disabled or the messages are free.
    """

    def __init__(
        self,
        *,
        is_enabled: bool,
        paid_message_star_count: int
    ):

        super().__init__()

        self.is_enabled = is_enabled
        self.paid_message_star_count = paid_message_star_count

    @staticmethod
    def _parse(
        action: "raw.types.MessageActionPaidMessagesPrice"
    ) -> "DirectMessagePriceChanged":
        return DirectMessagePriceChanged(
            is_enabled=action.broadcast_messages_allowed,
            paid_message_star_count=action.stars
        )
