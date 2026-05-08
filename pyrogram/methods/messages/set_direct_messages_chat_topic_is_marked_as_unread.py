
from datetime import datetime
from typing import Union

import pyrogram
from pyrogram import raw


class SetDirectMessagesChatTopicIsMarkedAsUnread:
    async def set_direct_messages_chat_topic_is_marked_as_unread(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        topic_id: int = None,
        is_marked_as_unread: bool = True
    ) -> int:
        """Change the marked as unread state of the topic in a channel direct messages chat administered by the current user.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            topic_id (``int``):
                Identifier of the topic which messages will be fetched.

            is_marked_as_unread (``bool``, *optional*):
                Pass True to mark the topic as unread.
                Pass False to mark the topic as read.
                Defaults to True.

        Returns:
            ``bool``: True on success

        Example:
            .. code-block:: python

                await app.set_direct_messages_chat_topic_is_marked_as_unread(chat_id, topic_id)
        """
        r = await self.invoke(
            raw.functions.messages.MarkDialogUnread(
                parent_peer=await self.resolve_peer(chat_id),
                peer=await self.resolve_peer(topic_id),
                unread=is_marked_as_unread
            )
        )

        return r
