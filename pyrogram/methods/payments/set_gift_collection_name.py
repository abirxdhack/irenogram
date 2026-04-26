from typing import Union

import pyrogram
from pyrogram import raw, types


class SetGiftCollectionName:
    async def set_gift_collection_name(
        self: "pyrogram.Client",
        owner_id: Union[int, str],
        collection_id: int,
        name: str
    ) -> "types.GiftCollection":
        """Changes name of a gift collection.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            owner_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".

            collection_id (``int``):
                Identifier of the gift collection.

            name (``str``):
                New name of the collection, 1-12 characters.

        Returns:
            :obj:`~pyrogram.types.GiftCollection`: On success, a updated collection is returned.

        Example:
            .. code-block:: python

                await set_gift_collection_name("me", 123, "My best gifts!")
        """
        r = await self.invoke(
            raw.functions.payments.UpdateStarGiftCollection(
                peer=await self.resolve_peer(owner_id),
                collection_id=collection_id,
                title=name
            )
        )

        return await types.GiftCollection._parse(self, r)
