
from typing import Union

import pyrogram
from pyrogram import raw

class DeleteStoryAlbum:
    async def delete_story_album(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        album_id: int,
    ) -> bool:
        """Delete a story album.

        The stories inside the album are not deleted — only the album itself
        is removed.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier or username of the peer who owns the album.

            album_id (``int``):
                ID of the album to delete.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.delete_story_album("me", album_id=1)
        """
        peer = await self.resolve_peer(chat_id)

        return await self.invoke(
            raw.functions.stories.DeleteAlbum(
                peer=peer,
                album_id=album_id,
            )
        )
