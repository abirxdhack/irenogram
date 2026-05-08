
import logging
from typing import List

import pyrogram
from pyrogram import raw
from pyrogram import types

log = logging.getLogger(__name__)


class GetStickers:
    async def get_stickers(
        self: "pyrogram.Client",
        short_name: str
    ) -> List["types.Sticker"]:
        """Get all stickers from set by short name.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            short_name (``str``):
                Short name of the sticker set, serves as the unique identifier for the sticker set.

        Returns:
            List of :obj:`~pyrogram.types.Sticker`: A list of stickers is returned.

        Example:
            .. code-block:: python

                await app.get_stickers("short_name")

        Raises:
            :raises ValueError: In case of invalid arguments.
        """
        sticker_set = await self.invoke(
            raw.functions.messages.GetStickerSet(
                stickerset=raw.types.InputStickerSetShortName(short_name=short_name),
                hash=0
            )
        )

        return types.List(
            [
                await types.Sticker._parse(self, doc, {type(a): a for a in doc.attributes})
                for doc in sticker_set.documents
            ]
        )
