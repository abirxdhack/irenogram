
import pyrogram
from pyrogram import raw, types


class CheckBotUsername:
    async def check_bot_username(
        self: "pyrogram.Client",
        username: str,
    ) -> "types.User":
        """Checks whether a username can be set for a new bot.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            username (``str``):
                Username to be checked.

        Returns:
            ``bool``: On success, True is returned.
        """
        return await self.invoke(raw.functions.bots.CheckUsername(username=username))
