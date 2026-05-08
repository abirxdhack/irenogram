
from typing import Union

import pyrogram
from pyrogram import raw
from pyrogram import types


class ApplyBoost:
    async def apply_boost(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
    ) -> bool:
        """Apply boost

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

        Returns:
            :obj:`~pyrogram.types.MyBoost`: On success, a boost object is returned.

        Example:
            .. code-block:: python

                await app.apply_boost(chat_id)
        """
        r = await self.invoke(
            raw.functions.premium.ApplyBoost(
                peer=await self.resolve_peer(chat_id),
            )
        )

        return types.MyBoost._parse(
            self,
            r.my_boosts[0],
            {i.id: i for i in r.users},
            {i.id: i for i in r.chats}
        )
