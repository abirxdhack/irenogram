
from typing import AsyncGenerator, Union

import pyrogram
from pyrogram import raw
from pyrogram import types
from pyrogram import utils


class GetPinnedStories:
    async def get_pinned_stories(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        offset_id: int = 0,
        limit: int = 0,
    ) -> AsyncGenerator["types.Story", None]:
        """Get all pinned stories from a chat by using chat identifier.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            offset_id (``int``, *optional*):
                Offset event identifier from which to start returning results.
                By default, no offset is applied and events will be returned starting from the latest.

            limit (``int``, *optional*):
                Maximum amount of events to be returned.
                By default, all events will be returned.

        Returns:
            ``Generator``: On success, a generator yielding :obj:`~pyrogram.types.Story` objects is returned.

        Example:
            .. code-block:: python

                async for story in app.get_pinned_stories(chat_id):
                    print(story)
        """
        current = 0
        total = abs(limit) or (1 << 31)
        limit = min(100, total)

        peer = await self.resolve_peer(chat_id)

        while True:
            r = await self.invoke(
                raw.functions.stories.GetPinnedStories(
                    peer=peer,
                    offset_id=offset_id,
                    limit=limit
                )
            )

            if not r.stories:
                return

            users = {i.id: i for i in r.users}
            chats = {i.id: i for i in r.chats}

            if isinstance(peer, raw.types.InputPeerChannel):
                peer_id = utils.get_raw_peer_id(peer)
                if peer_id not in r.chats:
                    channel = await self.invoke(raw.functions.channels.GetChannels(id=[peer]))
                    chats.update({peer_id: channel.chats[0]})

            last = r.stories[-1]
            offset_id = last.id

            for story in r.stories:
                yield await types.Story._parse(
                    self,
                    story,
                    peer,
                    users,
                    chats
                )

                current += 1

                if current >= total:
                    return
