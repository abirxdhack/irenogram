
from typing import Union

import pyrogram
from pyrogram import raw
from pyrogram import types


class GetBoosts:
    async def get_boosts(
        self: "pyrogram.Client",
    ) -> bool:
        """Get your boosts list

        .. include:: /_includes/usable-by/users.rst

        Returns:
            List of :obj:`~pyrogram.types.MyBoost`: On success.

        Example:
            .. code-block:: python

                await app.get_boosts()
        """
        r = await self.invoke(
            raw.functions.premium.GetMyBoosts()
        )

        users = {i.id: i for i in r.users}
        chats = {i.id: i for i in r.chats}

        return types.List(
            types.MyBoost._parse(
                self,
                boost,
                users,
                chats,
            ) for boost in r.my_boosts
        )
