import re
from typing import List, Union

import pyrogram
from pyrogram import raw, types, utils


class AddCollectionGifts:
    async def add_collection_gifts(
        self: "pyrogram.Client",
        owner_id: Union[int, str],
        collection_id: int,
        gift_ids: List[str]
    ) -> "types.GiftCollection":
        """Adds gifts to the beginning of a previously created collection.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            owner_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".

            collection_id (``int``):
                Identifier of the gift collection.

            name (``str``):
                Name of the collection, 1-12 characters.

            gift_ids (List of ``str``):
                Identifier of the gifts to add to the collection.

        Returns:
            :obj:`~pyrogram.types.GiftCollection`: On success, a updated collection is returned.

        Example:
            .. code-block:: python

                await app.add_collection_gifts("me", 123, ["https://t.me/nft/NekoHelmet-9215"])
        """
        stargifts = []

        for gift in gift_ids:
            stargifts.append(await utils.get_input_stargift(self, gift))

        r = await self.invoke(
            raw.functions.payments.UpdateStarGiftCollection(
                peer=await self.resolve_peer(owner_id),
                collection_id=collection_id,
                add_stargift=stargifts
            )
        )

        return await types.GiftCollection._parse(self, r)
