
from typing import List, Union

import pyrogram
from pyrogram import raw, types, utils


class CreateGiftCollection:
    async def create_gift_collection(
        self: "pyrogram.Client",
        owner_id: Union[int, str],
        name: str,
        gift_ids: List[str]
    ) -> "types.GiftCollection":
        """Creates a collection from gifts on the current user's or a channel's profile page.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            owner_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".

            name (``str``):
                Name of the collection, 1-12 characters.

            gift_ids (List of ``str``):
                Identifier of the gifts to add to the collection.

        Returns:
            :obj:`~pyrogram.types.GiftCollection`: On success, a created collection is returned.

        Example:
            .. code-block:: python

                await create_gift_collection("me", "My best gifts!", ["https://t.me/nft/NekoHelmet-9215"])
        """
        r = await self.invoke(
            raw.functions.payments.CreateStarGiftCollection(
                peer=await self.resolve_peer(owner_id),
                title=name,
                stargift=[await utils.get_input_stargift(self, owned_gift_id) for owned_gift_id in gift_ids],
            )
        )

        return await types.GiftCollection._parse(self, r)
