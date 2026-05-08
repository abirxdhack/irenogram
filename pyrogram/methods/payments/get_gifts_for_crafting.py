
from typing import AsyncGenerator

import pyrogram
from pyrogram import raw, types


class GetGiftsForCrafting:
    async def get_gifts_for_crafting(
        self: "pyrogram.Client",
        regular_gift_id: int,
        limit: int = 0
    ) -> AsyncGenerator["types.Gift", None]:
        """Returns upgraded gifts of the current user that can be used to craft another gifts.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            regular_gift_id (``int``):
                Identifier of the regular gift that will be used for crafting.

            limit (``int``, *optional*):
                The maximum number of gifts to be returned.
                Must be positive and can't be greater than 100.

        Returns:
            ``Generator``: A generator yielding :obj:`~pyrogram.types.Gift` objects.
        """
        current = 0
        total = abs(limit) or (1 << 31) - 1
        limit = min(100, total)

        offset = ""

        while True:
            r = await self.invoke(
                raw.functions.payments.GetCraftStarGifts(
                    gift_id=regular_gift_id,
                    offset=offset,
                    limit=limit
                ),
                sleep_threshold=60
            )

            users = {i.id: i for i in r.users}
            chats = {i.id: i for i in r.chats}

            receiver = users.get(self.me.id) if self.me else None

            user_star_gifts = [
                await types.Gift._parse(self, gift, receiver, users=users, chats=chats)
                for gift in r.gifts
            ]

            if not user_star_gifts:
                return

            for gift in user_star_gifts:
                yield gift

                current += 1

                if current >= total:
                    return

            offset = r.next_offset

            if not offset:
                return
