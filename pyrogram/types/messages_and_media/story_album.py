
from typing import Optional, Union, List

import pyrogram
from pyrogram import raw, types
from ..object import Object

class StoryAlbum(Object):
    """A story album (collection of stories).


    Parameters:
        album_id (``int``): Unique album identifier.
        title (``str``): Album title.
        icon_photo (:obj:`~pyrogram.types.Photo`, *optional*): Album icon as photo.
        icon_video (:obj:`~pyrogram.types.Document`, *optional*): Album icon as video.
    """

    def __init__(self, *, client=None, album_id: int, title: str,
                 icon_photo=None, icon_video=None):
        super().__init__(client)
        self.album_id = album_id
        self.title = title
        self.icon_photo = icon_photo
        self.icon_video = icon_video

    @staticmethod
    async def _parse(client, album: "raw.types.StoryAlbum") -> "StoryAlbum":
        icon_photo = None
        icon_video = None
        if getattr(album, "icon_photo", None):
            icon_photo = types.Photo._parse(client, album.icon_photo, 0)
        if getattr(album, "icon_video", None):
            from pyrogram.types.messages_and_media import Document

            icon_video = await Document._parse(client, album.icon_video, "")
        return StoryAlbum(
            client=client,
            album_id=album.album_id,
            title=album.title,
            icon_photo=icon_photo,
            icon_video=icon_video,
        )
