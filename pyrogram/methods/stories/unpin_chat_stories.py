
from typing import List, Union, Iterable

import pyrogram
from pyrogram import raw
from pyrogram import types


class UnpinChatStories:
    async def unpin_chat_stories(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        stories_ids: Union[int, Iterable[int]]
    ) -> List[int]:
        """Unpin one or more stories in a chat by using stories identifiers.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".

            stories_ids (``int`` | Iterable of ``int``, *optional*):
                List of unique identifiers of the target stories.

        Returns:
            List of ``int``: List of pinned stories identifiers.

        Example:
            .. code-block:: python

                await app.unpin_chat_stories(chat_id, 123456789)

        """
        is_iterable = not isinstance(stories_ids, int)
        stories_ids = list(stories_ids) if is_iterable else [stories_ids]

        r = await self.invoke(
            raw.functions.stories.TogglePinned(
                peer=await self.resolve_peer(chat_id),
                id=stories_ids,
                pinned=False
            )
        )

        return types.List(r)
