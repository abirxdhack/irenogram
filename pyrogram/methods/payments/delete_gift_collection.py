
from typing import Union

import pyrogram
from pyrogram import raw, types


class DeleteGiftCollection:
    async def delete_gift_collection(
        self: "pyrogram.Client",
        owner_id: Union[int, str],
        collection_id: int
    ) -> "types.GiftCollection":
        """Deletes a gift collection.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            owner_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".

            collection_id (``int``):
                Identifier of the gift collection.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                await app.delete_gift_collection("me", 123)
        """
        r = await self.invoke(
            raw.functions.payments.DeleteStarGiftCollection(
                peer=await self.resolve_peer(owner_id),
                collection_id=collection_id
            )
        )

        return r
