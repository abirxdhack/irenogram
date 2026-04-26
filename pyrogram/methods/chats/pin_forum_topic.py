
import pyrogram
from pyrogram import raw
from typing import Union


class PinForumTopic:
    async def pin_forum_topic(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        topic_id: int
    ) -> bool:
        """Pin a forum topic.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            topic_id (``int``):
                Unique identifier (int) of the target forum topic.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                await app.pin_forum_topic(chat_id, topic_id)
        """
        await self.invoke(
            raw.functions.channels.UpdatePinnedForumTopic(
                channel=await self.resolve_peer(chat_id),
                topic_id=topic_id,
                pinned=True
            )
        )

        return True
