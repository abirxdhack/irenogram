
from typing import Union, List, Optional

import pyrogram
from pyrogram import raw, types

class UpdateStarGiftCollection:
    async def update_star_gift_collection(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        collection_id: int,
        title: str = None,
        add_gift_ids: List[int] = None,
        remove_gift_ids: List[int] = None,
        order: List[int] = None,
    ) -> "types.StarGiftCollection":
        """Update a star gift collection.


        Parameters:
            chat_id (``int`` | ``str``):
                The peer who owns the collection.

            collection_id (``int``):
                ID of the collection to update.

            title (``str``, *optional*):
                New title for the collection.

            add_gift_ids (List of ``int``, *optional*):
                Saved gift IDs to add to the collection.

            remove_gift_ids (List of ``int``, *optional*):
                Saved gift IDs to remove from the collection.

            order (List of ``int``, *optional*):
                New order of saved gift IDs in the collection.

        Returns:
            :obj:`~pyrogram.types.StarGiftCollection`: The updated collection.
        """
        peer = await self.resolve_peer(chat_id)

        def make_input(ids):
            """Build the raw TL input object for this star gift collection update."""
            return [raw.types.InputSavedStarGiftUser(saved_id=i) for i in ids] if ids else None

        r = await self.invoke(
            raw.functions.payments.UpdateStarGiftCollection(
                peer=peer,
                collection_id=collection_id,
                title=title,
                add_stargift=make_input(add_gift_ids),
                delete_stargift=make_input(remove_gift_ids),
                order=make_input(order),
            )
        )
        return await types.StarGiftCollection._parse(self, r)
