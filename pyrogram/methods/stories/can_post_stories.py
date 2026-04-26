
from typing import Union

import pyrogram
from pyrogram import raw


class CanPostStories:
    async def can_post_stories(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
    ) -> int:
        """Check whether we can post stories as the specified chat.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

        Returns:
            ``int``: On success, count of remaining stories that can be posted is returned.

        Example:
            .. code-block:: python

                await app.can_post_stories(chat_id)
        """
        r = await self.invoke(
            raw.functions.stories.CanSendStory(
                peer=await self.resolve_peer(chat_id),
            )
        )

        return r.count_remains
