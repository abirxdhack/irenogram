
import logging
from typing import Union, Optional, AsyncGenerator

import pyrogram
from pyrogram import raw
from pyrogram import types

log = logging.getLogger(__name__)

class GetForumTopicsCount:
    async def get_forum_topics_count(
        self: "pyrogram.Client",
        chat_id: Union[int, str]
    ) -> Optional[AsyncGenerator["types.ForumTopic", None]]:
        """Get forum topics count from a chat.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                You can also use chat public link in form of *t.me/<username>* (str).

        Returns:
            ``int``: On success, the count of forum topics is returned.

        Example:
            .. code-block:: python


                app.get_forum_topics_count(chat_id)

        Raises:
            :raises ValueError: In case of invalid arguments.
        """

        peer = await self.resolve_peer(chat_id)

        rpc = raw.functions.channels.GetForumTopics(channel=peer, offset_date=0, offset_id=0, offset_topic=0, limit=0)

        r = await self.invoke(rpc, sleep_threshold=-1)

        return r.count
