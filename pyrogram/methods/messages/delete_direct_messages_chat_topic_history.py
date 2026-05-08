
from datetime import datetime
from typing import Union

import pyrogram
from pyrogram import raw, utils


class DeleteDirectMessagesChatTopicHistory:
    async def delete_direct_messages_chat_topic_history(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        topic_id: int = None,
        max_id: int = 0,
        min_date: datetime = None,
        max_date: datetime = None,
    ) -> int:
        """Delete messages in the topic in a channel direct messages chat administered by the current user.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            topic_id (``int``):
                Identifier of the topic which messages will be fetched.

            max_id (``int``, *optional*):
                Maximum ID of message to delete.

            min_date (:py:obj:`~datetime.datetime`, *optional*):
                Delete all messages newer than this time.

            max_date (:py:obj:`~datetime.datetime`, *optional*):
                Delete all messages older than this time.

        Returns:
            ``int``: Amount of affected messages

        Example:
            .. code-block:: python

                await app.delete_direct_messages_chat_topic_history(chat_id, topic_id)
        """
        r = await self.invoke(
            raw.functions.messages.DeleteSavedHistory(
                parent_peer=await self.resolve_peer(chat_id),
                peer=await self.resolve_peer(topic_id),
                max_id=max_id,
                min_date=utils.datetime_to_timestamp(min_date),
                max_date=utils.datetime_to_timestamp(max_date)
            )
        )

        return r.pts_count
