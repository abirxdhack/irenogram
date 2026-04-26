
from typing import Union, List

import pyrogram
from pyrogram import raw

class ReorderStarGiftCollections:
    async def reorder_star_gift_collections(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        order: List[int],
    ) -> bool:
        """Reorder star gift collections.


        Parameters:
            chat_id (``int`` | ``str``):
                The peer who owns the collections.

            order (List of ``int``):
                New order of collection IDs.

        Returns:
            ``bool``: True on success.
        """
        peer = await self.resolve_peer(chat_id)
        return await self.invoke(
            raw.functions.payments.ReorderStarGiftCollections(peer=peer, order=order)
        )
