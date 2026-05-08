
from typing import Union

import pyrogram
from pyrogram import raw


class ReadMentions:
    async def read_mentions(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        topic_id: int = None
    ) -> bool:
        """Mark a mention in the chat as read.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            topic_id (``int``, *optional*):
                Mark as read only mentions to messages within the specified forum topic.
                By default, no topic is applied and all mentions marked as read.

        Returns:
            ``bool`` - On success, True is returned.

        Example:
            .. code-block:: python

                await app.read_mentions(chat_id)

                await app.read_mentions(chat_id, topic_id)
        """
        r = await self.invoke(
            raw.functions.messages.ReadMentions(
                peer=await self.resolve_peer(chat_id),
                top_msg_id=topic_id
            )
        )

        return bool(r)
