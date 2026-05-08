from typing import List, Union

import pyrogram
from pyrogram import raw, types


class ReorderGiftCollections:
    async def reorder_gift_collections(
        self: "pyrogram.Client",
        owner_id: Union[int, str],
        collection_ids: List[int]
    ) -> "types.GiftCollection":
        """Changes order of gift collections.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            owner_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".

            gift_ids (List of ``int``):
                New order of gift collections.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                await app.reorder_gift_collections("me", [123, 456])
        """
        r = await self.invoke(
            raw.functions.payments.ReorderStarGiftCollections(
                peer=await self.resolve_peer(owner_id),
                order=collection_ids
            )
        )

        return r
