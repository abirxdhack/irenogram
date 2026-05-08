
from typing import List
import pyrogram
from pyrogram import raw, types

class ListManagedBots:
    async def list_managed_bots(
        self: "pyrogram.Client",
    ) -> List["types.User"]:
        """Return the list of bots managed by the current bot or user.

        .. include:: /_includes/usable-by/users-bots.rst

        Returns:
            List of :obj:`~pyrogram.types.User`: On success, returns a list of
            user objects representing all bots owned/managed by the current account.

        Example:
            .. code-block:: python

                bots = await app.list_managed_bots()
                for bot in bots:
                    print(bot.id, bot.username)
        """
        bots = await self.invoke(raw.functions.bots.GetAdminedBots())

        return types.List([
            types.User._parse(self, b)
            for b in bots
        ])
