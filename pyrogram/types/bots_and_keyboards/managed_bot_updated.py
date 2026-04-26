
from typing import Dict

import pyrogram
from pyrogram import raw, types

from ..object import Object


class ManagedBotUpdated(Object):
    """This object contains information about the creation or token update of a bot that is managed by the current bot.

    Parameters:
        user (:obj:`~pyrogram.types.User`):
            User that created the bot.

        bot (:obj:`~pyrogram.types.User`):
            Information about the bot.
            Token of the bot can be fetched using the method :meth:`~pyrogram.Client.get_managed_bot_token`.
    """

    def __init__(
        self,
        *,
        user: "types.User",
        bot: "types.User",
    ):
        super().__init__()

        self.user = user
        self.bot = bot

    @staticmethod
    async def _parse(
        client: "pyrogram.Client",
        managed_bot_updated: "raw.types.UpdateManagedBot",
        users: Dict[int, "raw.types.User"],
    ) -> "ManagedBotUpdated":
        if not isinstance(managed_bot_updated, raw.types.UpdateManagedBot):
            return

        return ManagedBotUpdated(
            user=types.User._parse(client, users.get(managed_bot_updated.user_id)),
            bot=types.User._parse(client, users.get(managed_bot_updated.bot_id))
        )
