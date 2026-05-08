
from typing import List, Union

import pyrogram
from pyrogram import raw, types

class CreateStoryAlbum:
    async def create_story_album(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        title: str,
        story_ids: List[int] = None,
    ) -> "types.StoryAlbum":
        """Create a new story album for a user or channel.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier or username of the peer who owns the album.
                Use ``"me"`` or ``"self"`` for your own profile.

            title (``str``):
                Title of the new album.

            story_ids (List of ``int``, *optional*):
                IDs of stories to add to the album on creation.
                Pass an empty list or omit to create an empty album.

        Returns:
            :obj:`~pyrogram.types.StoryAlbum`: The created story album.

        Example:
            .. code-block:: python

                album = await app.create_story_album("me", "Summer 2024")
                print(album.album_id, album.title)


                album = await app.create_story_album("me", "Highlights", story_ids=[101, 102])
        """
        peer = await self.resolve_peer(chat_id)

        r = await self.invoke(
            raw.functions.stories.CreateAlbum(
                peer=peer,
                title=title,
                stories=story_ids or [],
            )
        )

        return await types.StoryAlbum._parse(self, r)
