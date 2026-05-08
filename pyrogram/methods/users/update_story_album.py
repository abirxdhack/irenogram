
from typing import List, Optional, Union

import pyrogram
from pyrogram import raw, types

class UpdateStoryAlbum:
    async def update_story_album(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        album_id: int,
        title: str = None,
        add_story_ids: List[int] = None,
        delete_story_ids: List[int] = None,
        order: List[int] = None,
    ) -> "types.StoryAlbum":
        """Update a story album's title, contents, or story order.

        All parameters except ``chat_id`` and ``album_id`` are optional.
        Only the fields you pass will be changed.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier or username of the peer who owns the album.

            album_id (``int``):
                ID of the album to update.

            title (``str``, *optional*):
                New title for the album.

            add_story_ids (List of ``int``, *optional*):
                IDs of stories to add to the album.

            delete_story_ids (List of ``int``, *optional*):
                IDs of stories to remove from the album.

            order (List of ``int``, *optional*):
                New ordered list of story IDs inside the album.

        Returns:
            :obj:`~pyrogram.types.StoryAlbum`: The updated album.

        Example:
            .. code-block:: python


                await app.update_story_album("me", album_id=1, title="Best of 2024")


                await app.update_story_album("me", album_id=1, add_story_ids=[105, 106])


                await app.update_story_album("me", album_id=1, delete_story_ids=[101])
        """
        peer = await self.resolve_peer(chat_id)

        r = await self.invoke(
            raw.functions.stories.UpdateAlbum(
                peer=peer,
                album_id=album_id,
                title=title,
                add_stories=add_story_ids,
                delete_stories=delete_story_ids,
                order=order,
            )
        )

        return await types.StoryAlbum._parse(self, r)
