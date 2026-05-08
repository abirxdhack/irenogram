
from datetime import datetime
from typing import AsyncGenerator, Optional

import pyrogram
from pyrogram import raw, types, utils

class SearchGlobalHashtagMessages:
    async def search_global_hashtag_messages(
        self: "pyrogram.Client",
        hashtag: str = "",
        query: str = None,
        offset_id: int = 0,
        offset_date: datetime = utils.zero_datetime(),
        limit: int = 0,
        allow_paid_stars: int = None,
    ) -> AsyncGenerator["types.Message", None]:
        """Search public channel posts with a given hashtag and/or text query.

        For the count only, see :meth:`~pyrogram.Client.search_global_hashtag_messages_count`.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            hashtag (``str``, *optional*):
                Hashtag to search for.

            query (``str``, *optional*):
                Additional free-text search query (Layer 207+).

            offset_id (``int``, *optional*):
                Offset message ID for pagination.

            offset_date (:py:obj:`~datetime.datetime`, *optional*):
                Return only messages older than this date.

            limit (``int``, *optional*):
                Maximum number of messages to return.
                Defaults to ``0`` (no limit).

            allow_paid_stars (``int``, *optional*):
                Maximum Stars budget for paid-broadcast results (Layer 207+).
                Pass ``None`` to exclude paid results.

        Returns:
            ``AsyncGenerator``: Yields :obj:`~pyrogram.types.Message` objects.

        Example:
            .. code-block:: python

                async for message in app.search_global_hashtag_messages("#pyrogram"):
                    print(message.text)
        """
        current = 0
        total = abs(limit) or (1 << 31)
        limit = min(100, total)

        offset_peer = raw.types.InputPeerEmpty()

        while True:
            messages = await utils.parse_messages(
                self,
                await self.invoke(
                    raw.functions.channels.SearchPosts(
                        hashtag=hashtag or None,
                        query=query,
                        offset_rate=utils.datetime_to_timestamp(offset_date),
                        offset_peer=offset_peer,
                        offset_id=offset_id,
                        limit=limit,
                        allow_paid_stars=allow_paid_stars,
                    ),
                    sleep_threshold=60,
                ),
                replies=0,
            )

            if not messages:
                return

            last = messages[-1]
            offset_date = utils.datetime_to_timestamp(last.date)
            offset_peer = await self.resolve_peer(last.chat.id)
            offset_id = last.id

            for message in messages:
                yield message

                current += 1

                if current >= total:
                    return
