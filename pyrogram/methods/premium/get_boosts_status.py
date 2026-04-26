
from typing import Union

import pyrogram
from pyrogram import raw, types


class GetBoostsStatus:
    async def get_boosts_status(
        self: "pyrogram.Client",
        chat_id: Union[int, str]
    ) -> "types.BoostsStatus":
        """Get boosts status of channel

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

        Returns:
            :obj:`~pyrogram.types.BoostsStatus`: On success.
        """
        r = await self.invoke(
            raw.functions.premium.GetBoostsStatus(peer=await self.resolve_peer(chat_id))
        )

        return types.BoostsStatus._parse(r)
