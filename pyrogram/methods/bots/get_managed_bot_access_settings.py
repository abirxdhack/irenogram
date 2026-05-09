from typing import Union

import pyrogram
from pyrogram import raw, types


class GetManagedBotAccessSettings:
    async def get_managed_bot_access_settings(
        self: "pyrogram.Client",
        user_id: Union[int, str],
    ) -> "types.BotAccessSettings":
        """Use this method to get the access settings of a managed bot.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the managed bot whose access settings will be returned.

        Returns:
            :obj:`~pyrogram.types.BotAccessSettings`: On success, bot access settings are returned.

        Example:
            .. code-block:: python

                settings = await app.get_managed_bot_access_settings("my_bot")
                print(settings.is_access_restricted)
        """

        r = await self.invoke(
            raw.functions.bots.GetAccessSettings(
                bot=await self.resolve_peer(user_id),
            )
        )

        return types.BotAccessSettings._parse(self, r)