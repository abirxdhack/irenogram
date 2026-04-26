
from typing import Union

import pyrogram
from pyrogram import raw, types

class DeletePollAnswer:
    async def delete_poll_answer(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int,
        option: Union[int, bytes],
    ) -> "types.Message":
        """Delete a dynamically added answer option from a poll.

        This feature is part of Bot API 9.6 poll revolution — only works on polls
        where ``open_answers`` is True and only the user who added the option can remove it.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            message_id (``int``):
                Identifier of the message containing the poll.

            option (``int`` | ``bytes``):
                The poll option to delete — either its 0-based index (int) or raw option bytes.

        Returns:
            :obj:`~pyrogram.types.Message`: On success, the updated poll message is returned.

        Example:
            .. code-block:: python

                await app.delete_poll_answer(chat_id, message_id, 3)
        """
        if isinstance(option, int):
            poll_message = await self.get_messages(chat_id, message_id)
            option_bytes = poll_message.poll.options[option].data
        else:
            option_bytes = option

        r = await self.invoke(
            raw.functions.messages.DeletePollAnswer(
                peer=await self.resolve_peer(chat_id),
                msg_id=message_id,
                option=option_bytes,
            )
        )

        for update in r.updates:
            if isinstance(
                update,
                (
                    raw.types.UpdateNewMessage,
                    raw.types.UpdateNewChannelMessage,
                    raw.types.UpdateEditMessage,
                    raw.types.UpdateEditChannelMessage,
                ),
            ):
                return await types.Message._parse(
                    self,
                    update.message,
                    {u.id: u for u in r.users},
                    {c.id: c for c in r.chats},
                )

        return None
