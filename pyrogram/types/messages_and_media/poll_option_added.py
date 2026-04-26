
from typing import Optional

import pyrogram
from pyrogram import raw, types

from ..object import Object


class PollOptionAdded(Object):
    """Describes a service message about an option added to a poll.

    Parameters:
        poll_message (:obj:`~pyrogram.types.Message`, *optional*):
            Message containing the poll to which the option was added, if known.

        option_persistent_id (``str``):
            Unique identifier of the added option.

        text (:obj:`~pyrogram.types.FormattedText`, *optional*):
            Option text.
    """

    def __init__(
        self,
        *,
        poll_message: Optional["types.Message"] = None,
        option_persistent_id: str,
        text: "types.FormattedText"
    ):
        super().__init__()

        self.poll_message = poll_message
        self.option_persistent_id = option_persistent_id
        self.text = text

    @staticmethod
    async def _parse(
        client: "pyrogram.Client",
        reply_message: Optional["types.Message"],
        poll_option_added: "raw.types.MessageActionPollAppendAnswer",
    ) -> "PollOptionAdded":
        if not isinstance(poll_option_added, raw.types.MessageActionPollAppendAnswer):
            return

        answer = poll_option_added.answer

        return PollOptionAdded(
            poll_message=reply_message,
            option_persistent_id=answer.option.decode(),
            text=types.FormattedText._parse(client, answer.text)
        )
