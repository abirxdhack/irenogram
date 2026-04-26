from typing import List, Union

import pyrogram
from pyrogram import raw, types


class GetGiftCollections:
    async def get_gift_collections(
        self: "pyrogram.Client",
        owner_id: Union[int, str]
    ) -> List["types.GiftCollection"]:
        """Returns collections of gifts owned by the given user or chat.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            owner_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".

        Returns:
            List of :obj:`~pyrogram.types.GiftCollection`: On success, a list of collections is returned.
        """
        r = await self.invoke(
            raw.functions.payments.GetStarGiftCollections(
                peer=await self.resolve_peer(owner_id),
                hash=0
            )
        )

        return types.List(
            [
                await types.GiftCollection._parse(self, collection)
                for collection in r.collections
            ]
        )
