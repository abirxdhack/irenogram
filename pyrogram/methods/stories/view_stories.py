
from typing import Union, List

import pyrogram
from pyrogram import raw


class ViewStories:
    async def view_stories(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        story_id: Union[int, List[int]],
    ) -> bool:
        """Increment story views.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For a contact that exists in your Telegram address book you can use his phone number (str).

            story_id (``int`` | List of ``int``):
                Identifier or list of story identifiers of the target story.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                await app.view_stories(chat_id, 1)
        """
        ids = [story_id] if not isinstance(story_id, list) else story_id

        r = await self.invoke(
            raw.functions.stories.IncrementStoryViews(
                peer=await self.resolve_peer(chat_id),
                id=ids
            )
        )

        return r
