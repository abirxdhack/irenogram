
from typing import AsyncGenerator, Optional

import pyrogram
from pyrogram import raw, enums
from pyrogram import types
from pyrogram import utils

class SearchGlobal:
    async def search_global(
        self: "pyrogram.Client",
        query: str = "",
        filter: "enums.MessagesFilter" = enums.MessagesFilter.EMPTY,
        channels_only: Optional[bool] = None,
        groups_only: Optional[bool] = None,
        users_only: Optional[bool] = None,
        limit: int = 0,
    ) -> Optional[AsyncGenerator["types.Message", None]]:
        """Search messages globally from all of your chats.

        If you want to get the messages count only, see :meth:`~pyrogram.Client.search_global_count`.

        .. note::

            Due to server-side limitations, you can only get up to around ~10,000 messages and each message
            retrieved will not have any *reply_to_message* field.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            query (``str``, *optional*):
                Text query string.
                Use "@" to search for mentions.

            filter (:obj:`~pyrogram.enums.MessagesFilter`, *optional*):
                Pass a filter in order to search for specific kind of messages only.
                Defaults to any message (no filter).

            limit (``int``, *optional*):
                Limits the number of messages to be retrieved.
                By default, no limit is applied and all messages are returned.

            channels_only (``bool``, *optional*):
                Pass True to search only in channels.

            groups_only (``bool``, *optional*):
                Pass True to search only in groups.

            users_only (``bool``, *optional*):
                Pass True to search only in users.

        Returns:
            ``Generator``: A generator yielding :obj:`~pyrogram.types.Message` objects.

        Example:
            .. code-block:: python

                from pyrogram import enums


                async for message in app.search_global("pyrogram", limit=50):
                    print(message.text)


                async for message in app.search_global(filter=enums.MessagesFilter.PHOTO, limit=20):
                    print(message.photo)
        """
        current = 0

        total = abs(limit) or (1 << 31)
        limit = min(100, total)

        offset_date = 0
        offset_peer = raw.types.InputPeerEmpty()
        offset_id = 0

        while True:
            messages = await utils.parse_messages(
                self,
                await self.invoke(
                    raw.functions.messages.SearchGlobal(
                        q=query,
                        filter=filter.value(),
                        min_date=0,
                        max_date=0,
                        offset_rate=offset_date,
                        offset_peer=offset_peer,
                        offset_id=offset_id,
                        broadcasts_only=channels_only,
                        groups_only=groups_only,
                        users_only=users_only,
                        limit=limit
                    ),
                    sleep_threshold=60
                ),
                replies=0
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
