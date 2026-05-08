
from typing import List

import pyrogram
from pyrogram import raw, types


class GetSuitableDiscussionChats:
    async def get_suitable_discussion_chats(
        self: "pyrogram.Client"
    ) -> List["types.Chat"]:
        """Return a list of basic group and supergroup chats, which can be used as a discussion group for a channel.

        Returned basic group chats must be first upgraded to supergroups before they can be set as a discussion group.

        .. include:: /_includes/usable-by/users.rst

        Returns:
            List of :obj:`~pyrogram.types.Chat`: List of suitable discussion chats.

        Example:
            .. code-block:: python

                chats = await app.get_suitable_discussion_chats()
        """
        r = await self.invoke(
            raw.functions.channels.GetGroupsForDiscussion()
        )

        return types.List([types.Chat._parse_chat(self, i) for i in r.chats])
