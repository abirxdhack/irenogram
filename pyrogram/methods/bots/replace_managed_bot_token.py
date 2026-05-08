
from typing import Union

import pyrogram
from pyrogram import raw


class ReplaceManagedBotToken:
    async def replace_managed_bot_token(
        self: "pyrogram.Client",
        user_id: Union[int, str],
    ) -> str:
        """Use this method to revoke the current token of a managed bot and generate a new one.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the managed bot whose token will be replaced.

        Returns:
            ``str``: On success, new bot token is returned.
        """
        r = await self.invoke(
            raw.functions.bots.ExportBotToken(
                bot=await self.resolve_peer(user_id),
                revoke=True
            )
        )

        return r.token
