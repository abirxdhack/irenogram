from typing import List

import pyrogram
from pyrogram import raw, types


class GetAvailableGifts:
    async def get_available_gifts(
        self: "pyrogram.Client",
    ) -> List["types.Gift"]:
        """Get all available star gifts that can be sent to other users.

        .. include:: /_includes/usable-by/users-bots.rst

        Returns:
            List of :obj:`~pyrogram.types.Gift`: On success, a list of star gifts is returned.

        Example:
            .. code-block:: python

                await app.get_available_gifts()
        """
        r = await self.invoke(
            raw.functions.payments.GetStarGifts(hash=0)
        )

        users = {i.id: i for i in r.users}
        chats = {i.id: i for i in r.chats}

        return types.List([await types.Gift._parse_regular(self, gift, users=users, chats=chats) for gift in r.gifts])
