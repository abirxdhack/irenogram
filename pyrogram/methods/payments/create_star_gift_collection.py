
from typing import Union, List

import pyrogram
from pyrogram import raw, types

class CreateStarGiftCollection:
    async def create_star_gift_collection(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        title: str,
        saved_gift_ids: List[int] = None,
    ) -> "types.StarGiftCollection":
        """Create a new star gift collection.


        Parameters:
            chat_id (``int`` | ``str``):
                The peer who owns the collection (yourself or a channel you manage).

            title (``str``):
                Title of the new collection.

            saved_gift_ids (List of ``int``, *optional*):
                Saved gift IDs to add to the collection.

        Returns:
            :obj:`~pyrogram.types.StarGiftCollection`: The created collection.

        Example:
            .. code-block:: python

                col = await app.create_star_gift_collection("me", "My Favorites")
        """
        peer = await self.resolve_peer(chat_id)
        saved_gifts = [
            raw.types.InputSavedStarGiftUser(saved_id=gid)
            for gid in (saved_gift_ids or [])
        ]
        r = await self.invoke(
            raw.functions.payments.CreateStarGiftCollection(
                peer=peer,
                title=title,
                stargift=saved_gifts,
            )
        )
        return await types.StarGiftCollection._parse(self, r)
