
from typing import Optional
import pyrogram
from pyrogram import raw
from ..object import Object

class StarGiftCollection(Object):
    """A collection of star gifts belonging to a user or channel.


    Parameters:
        collection_id (``int``): Unique collection identifier.
        title (``str``): Display title of the collection.
        gifts_count (``int``): Number of gifts in the collection.
        hash (``int``): Hash for caching.
        icon (:obj:`~pyrogram.types.Document`, *optional*): Collection icon document.
    """

    def __init__(self, *, client=None, collection_id: int, title: str,
                 gifts_count: int, hash: int, icon=None):
        super().__init__(client)
        self.collection_id = collection_id
        self.title = title
        self.gifts_count = gifts_count
        self.hash = hash
        self.icon = icon

    @staticmethod
    async def _parse(client, col: "raw.types.StarGiftCollection") -> "StarGiftCollection":
        icon = None
        if getattr(col, "icon", None):

            from pyrogram.types.messages_and_media import Document
            icon = await Document._parse(client, col.icon, {})
        return StarGiftCollection(
            client=client,
            collection_id=col.collection_id,
            title=col.title,
            gifts_count=col.gifts_count,
            hash=col.hash,
            icon=icon,
        )
