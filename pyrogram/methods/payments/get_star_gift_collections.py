
from typing import Union, List

import pyrogram
from pyrogram import raw, types

class GetStarGiftCollections:
    async def get_star_gift_collections(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
    ) -> List["types.StarGiftCollection"]:
        """Get star gift collections of a user or channel.


        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier or username of the target peer.

        Returns:
            List of :obj:`~pyrogram.types.StarGiftCollection`: On success.

        Example:
            .. code-block:: python

                collections = await app.get_star_gift_collections("me")
        """
        peer = await self.resolve_peer(chat_id)
        r = await self.invoke(
            raw.functions.payments.GetStarGiftCollections(peer=peer, hash=0)
        )
        if isinstance(r, raw.types.payments.StarGiftCollectionsNotModified):
            return []
        return [
            await types.StarGiftCollection._parse(self, col)
            for col in r.collections
        ]
