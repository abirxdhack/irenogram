
from typing import List
import pyrogram
from pyrogram import raw, types

class GetOwnedBots:
    async def get_owned_bots(
        self: "pyrogram.Client",
    ) -> List["types.User"]:
        """Returns the list of bots owned by the current user.

        .. include:: /_includes/usable-by/users.rst

        Returns:
            List of :obj:`~pyrogram.types.User`: On success.

        Example:
            .. code-block:: python

                bots = await app.get_owned_bots()
        """

        bots = await self.invoke(raw.functions.bots.GetAdminedBots())
        return types.List([
            types.User._parse(self, b)
            for b in bots
        ])
