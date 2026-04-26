
from typing import Union

import pyrogram
from pyrogram import raw

class DeleteStarGiftCollection:
    async def delete_star_gift_collection(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        collection_id: int,
    ) -> bool:
        """Delete a star gift collection.


        Parameters:
            chat_id (``int`` | ``str``):
                The peer who owns the collection.

            collection_id (``int``):
                ID of the collection to delete.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.delete_star_gift_collection("me", collection_id=123)
        """
        peer = await self.resolve_peer(chat_id)
        return await self.invoke(
            raw.functions.payments.DeleteStarGiftCollection(
                peer=peer,
                collection_id=collection_id,
            )
        )
