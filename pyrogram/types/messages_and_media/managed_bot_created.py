
from typing import Dict

import pyrogram
from pyrogram import raw, types

from ..object import Object


class ManagedBotCreated(Object):
    """This object contains information about the bot that was created to be managed by the current bot.

    Parameters:
        bot (:obj:`~pyrogram.types.User`):
            Information about the bot.
            The bot's token can be fetched using the method :meth:`~pyrogram.Client.get_managed_bot_token`.
    """

    def __init__(
        self,
        *,
        bot: "types.User",
    ):
        super().__init__()

        self.bot = bot

    @staticmethod
    async def _parse(
        client: "pyrogram.Client",
        managed_bot_created: "raw.types.MessageActionManagedBotCreated",
        users: Dict[int, "raw.types.User"],
    ) -> "ManagedBotCreated":
        if not isinstance(managed_bot_created, raw.types.MessageActionManagedBotCreated):
            return

        return ManagedBotCreated(
            bot=types.User._parse(client, users.get(managed_bot_created.bot_id))
        )
