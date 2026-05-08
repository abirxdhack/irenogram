
from typing import AsyncGenerator, Union

import pyrogram
from pyrogram import raw
from pyrogram import types


class GetChatStories:
    async def get_chat_stories(
        self: "pyrogram.Client",
        chat_id: Union[int, str]
    ) -> AsyncGenerator["types.Story", None]:
        """Get all non expired stories from a chat by using chat identifier.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.
                For your personal story you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

        Returns:
            ``Generator``: On success, a generator yielding :obj:`~pyrogram.types.Story` objects is returned.

        Example:
            .. code-block:: python

                async for story in app.get_chat_stories(chat_id):
                    print(story)

        Raises:
            :raises ValueError: In case of invalid arguments.
        """
        peer = await self.resolve_peer(chat_id)

        r = await self.invoke(
            raw.functions.stories.GetPeerStories(
                peer=peer
            )
        )

        users = {i.id: i for i in r.users}
        chats = {i.id: i for i in r.chats}

        for story in r.stories.stories:
            yield await types.Story._parse(
                self,
                story,
                r.stories.peer,
                users,
                chats
            )
