
from typing import AsyncGenerator, Optional

import pyrogram
from pyrogram import raw, types, utils

class SearchChannelPosts:
    async def search_channel_posts(
        self: "pyrogram.Client",
        hashtag: str = None,
        query: str = None,
        limit: int = 0,
        allow_paid_stars: int = None,
    ) -> Optional[AsyncGenerator["types.Message", None]]:
        """Search posts across all public channels by hashtag or text query.

        This method calls ``channels.searchPosts`` (TL Layer 207+).
        At least one of ``hashtag`` or ``query`` must be provided.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            hashtag (``str``, *optional*):
                Hashtag to search for (without the ``
                At least one of ``hashtag`` or ``query`` must be set.

            query (``str``, *optional*):
                Free-text search query.
                At least one of ``hashtag`` or ``query`` must be set.

            limit (``int``, *optional*):
                Maximum number of messages to return.
                Defaults to 0 (no limit — all results are fetched).

            allow_paid_stars (``int``, *optional*):
                Maximum amount of Stars the user agrees to spend to view
                pay-walled posts (pass ``0`` to skip paid posts entirely).

        Yields:
            :obj:`~pyrogram.types.Message`: Matching channel post messages.

        Raises:
            :raises ValueError: If neither ``hashtag`` nor ``query`` is provided.

        Example:
            .. code-block:: python


                async for msg in app.search_channel_posts(hashtag="pyrogram"):
                    print(msg.text)


                async for msg in app.search_channel_posts(query="Telegram update", limit=50):
                    print(msg.chat.title, msg.text)
        """
        if not hashtag and not query:
            raise ValueError("At least one of 'hashtag' or 'query' must be provided.")

        current = 0
        total = abs(limit) or (1 << 31)

        batch = min(100, total)

        offset_rate = 0
        offset_peer = raw.types.InputPeerEmpty()
        offset_id = 0

        while True:
            r = await self.invoke(
                raw.functions.channels.SearchPosts(
                    hashtag=hashtag,
                    query=query,
                    offset_rate=offset_rate,
                    offset_peer=offset_peer,
                    offset_id=offset_id,
                    limit=batch,
                    allow_paid_stars=allow_paid_stars,
                ),
                sleep_threshold=60,
            )

            messages = await utils.parse_messages(self, r, replies=0)

            if not messages:
                return

            last = messages[-1]
            offset_rate = utils.datetime_to_timestamp(last.date)
            offset_peer = await self.resolve_peer(last.chat.id)
            offset_id = last.id

            for message in messages:
                yield message
                current += 1
                if current >= total:
                    return
