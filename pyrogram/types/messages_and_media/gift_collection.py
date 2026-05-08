from typing import Optional

import pyrogram
from pyrogram import raw, types

from ..object import Object


class GiftCollection(Object):
    """Describes collection of gifts.

    Parameters:
        id (``int``):
            Unique identifier of the collection.

        name (``str``):
            Name of the collection.

        gift_count (``int``):
            Total number of gifts in the collection.

        icon (:obj:`~pyrogram.types.Sticker`, *optional*):
            Icon of the collection.
    """
    def __init__(
        self, *,
        id: int,
        name: str,
        gift_count: int,
        icon: Optional["types.Sticker"] = None
    ):
        super().__init__()

        self.id = id
        self.name = name
        self.gift_count = gift_count
        self.icon = icon

    @staticmethod
    async def _parse(
        client: "pyrogram.Client",
        collection: "raw.types.StarGiftCollection"
    ) -> "GiftCollection":
        sticker = None

        if collection.icon:
            doc = collection.icon
            attributes = {type(i): i for i in doc.attributes}
            sticker = await types.Sticker._parse(client, doc, attributes)

        return GiftCollection(
            id=collection.collection_id,
            name=collection.title,
            gift_count=collection.gifts_count,
            icon=sticker
        )
