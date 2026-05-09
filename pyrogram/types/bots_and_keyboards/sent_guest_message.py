from pyrogram import raw, utils

from ..object import Object


class SentGuestMessage(Object):
    """Describes an inline message sent by a guest bot.

    Parameters:
        inline_message_id (``str``):
            Identifier of the sent inline message.
    """

    def __init__(
        self,
        *,
        inline_message_id: str,
    ):
        super().__init__()

        self.inline_message_id = inline_message_id

    @staticmethod
    def _parse(
        inline_message_id: "raw.base.InputBotInlineMessageID",
    ) -> "SentGuestMessage":
        return SentGuestMessage(
            inline_message_id=utils.pack_inline_message_id(inline_message_id)
        )