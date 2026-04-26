
from typing import List, Union, Iterable

import pyrogram
from pyrogram import raw
from pyrogram import types


class DeleteStories:
    async def delete_stories(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        story_ids: Union[int, Iterable[int]],
    ) -> List[int]:
        """Delete posted stories.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".

            story_ids (``int`` | Iterable of ``int``, *optional*):
                Unique identifier (int) or list of unique identifiers (list of int) for the target stories.

        Returns:
            List of ``int``: List of deleted stories IDs.

        Example:
            .. code-block:: python

                await app.delete_stories(chat_id, 1)

                await app.delete_stories(chat_id, [1, 2])
        """
        is_iterable = not isinstance(story_ids, int)
        ids = list(story_ids) if is_iterable else [story_ids]

        r = await self.invoke(
            raw.functions.stories.DeleteStories(
                peer=await self.resolve_peer(chat_id),
                id=ids
            )
        )

        return types.List(r)
