from typing import AsyncGenerator

import pyrogram
from pyrogram import enums, raw, types, utils


class GetTopChats:
    async def get_top_chats(
        self: "pyrogram.Client",
        category: "enums.TopChatCategory",
        limit: int = 0,
    ) -> AsyncGenerator["types.Chat", None]:
        """Returns a list of frequently used chats.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            category (:obj:`~pyrogram.enums.TopChatCategory`):
                Category of chats to be returned.

            limit (``int``, *optional*):
                The maximum number of chats to be returned.
                By default, no limit is applied and all chats are returned.

        Returns:
            ``Generator``: A generator yielding :obj:`~pyrogram.types.Chat` objects.

        Example:
            .. code-block:: python

                async for chat in app.get_top_chats(enums.TopChatCategory.USERS):
                    print(chat.full_name)
        """
        current = 0
        total = limit or (1 << 31) - 1
        limit = min(30, total)

        offset = 0

        while True:
            r = await self.invoke(
                raw.functions.contacts.GetTopPeers(
                    offset=offset,
                    limit=limit,
                    hash=0,
                    correspondents=category == enums.TopChatCategory.USERS,
                    bots_pm=category == enums.TopChatCategory.BOTS,
                    bots_inline=category == enums.TopChatCategory.INLINE_BOTS,
                    phone_calls=category == enums.TopChatCategory.CALLS,
                    forward_users=category == enums.TopChatCategory.FORWARD_CHATS,
                    forward_chats=category == enums.TopChatCategory.FORWARD_CHATS,
                    groups=category == enums.TopChatCategory.GROUPS,
                    channels=category == enums.TopChatCategory.CHANNELS,
                    bots_app=category == enums.TopChatCategory.WEB_APP_BOTS,
                    bots_guestchat=category == enums.TopChatCategory.GUEST_BOTS,
                ),
                sleep_threshold=60
            )

            if not isinstance(r, raw.types.contacts.TopPeers):
                return

            users = {i.id: i for i in r.users}
            raw_chats = {i.id: i for i in r.chats}

            parsed_chats = []

            for cat in r.categories:
                for top_peer in cat.peers:
                    peer_id = utils.get_raw_peer_id(top_peer.peer)

                    parsed_chats.append(
                        types.Chat._parse_chat(self, users.get(peer_id) or raw_chats.get(peer_id))
                    )

            if not parsed_chats:
                return

            offset += len(parsed_chats)

            for chat in parsed_chats:
                yield chat

                current += 1

                if current >= total:
                    return