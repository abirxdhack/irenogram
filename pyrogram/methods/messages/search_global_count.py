
from typing import Optional

import pyrogram
from pyrogram import raw, enums

class SearchGlobalCount:
    async def search_global_count(
        self: "pyrogram.Client",
        query: str = "",
        filter: "enums.MessagesFilter" = enums.MessagesFilter.EMPTY,
        channels_only: Optional[bool] = None,
        groups_only: Optional[bool] = None,
        users_only: Optional[bool] = None,
    ) -> int:
        """Get the count of messages resulting from a global search.

        If you want to get the actual messages, see :meth:`~pyrogram.Client.search_global`.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            query (``str``, *optional*):
                Text query string.
                Use "@" to search for mentions.

            filter (:obj:`~pyrogram.enums.MessagesFilter`, *optional*):
                Pass a filter in order to search for specific kind of messages only:

            channels_only (``bool``, *optional*):
                Pass True to search only in channels.

            groups_only (``bool``, *optional*):
                Pass True to search only in groups.

            users_only (``bool``, *optional*):
                Pass True to search only in users.

        Returns:
            ``int``: On success, the messages count is returned.
        """
        r = await self.invoke(
            raw.functions.messages.SearchGlobal(
                q=query,
                filter=filter.value(),
                min_date=0,
                max_date=0,
                offset_rate=0,
                offset_peer=raw.types.InputPeerEmpty(),
                offset_id=0,
                broadcasts_only=channels_only,
                groups_only=groups_only,
                users_only=users_only,
                limit=1
            )
        )

        if hasattr(r, "count"):
            return r.count
        else:
            return len(r.messages)
