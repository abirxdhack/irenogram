
from typing import List, Union

import pyrogram
from pyrogram import raw, types

class GetStoryAlbums:
    async def get_story_albums(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
    ) -> List["types.StoryAlbum"]:
        """Get all story albums for a user or channel.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier or username of the target peer.
                Use ``"me"`` or ``"self"`` for your own profile.

        Returns:
            List of :obj:`~pyrogram.types.StoryAlbum`: All albums belonging to
            the peer. Returns an empty list if no albums exist.

        Example:
            .. code-block:: python

                albums = await app.get_story_albums("me")
                for album in albums:
                    print(album.album_id, album.title)
        """
        peer = await self.resolve_peer(chat_id)

        r = await self.invoke(
            raw.functions.stories.GetAlbums(peer=peer, hash=0)
        )

        if isinstance(r, raw.types.stories.AlbumsNotModified):
            return types.List()

        return types.List(
            [await types.StoryAlbum._parse(self, album) for album in r.albums]
        )
