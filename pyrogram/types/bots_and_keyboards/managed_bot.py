
from typing import Optional
import pyrogram
from pyrogram import raw, types
from ..object import Object

class ManagedBot(Object):
    """Represents a managed bot created by a manager bot.


    Parameters:
        user_id (``int``):
            Identifier of the manager user who owns this managed bot.

        bot_id (``int``):
            Identifier of the managed bot user.

        bot (:obj:`~pyrogram.types.User`, *optional*):
            Full user object of the managed bot, if available.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        user_id: int,
        bot_id: int,
        bot: Optional["types.User"] = None,
    ):
        super().__init__(client)

        self.user_id = user_id
        self.bot_id = bot_id
        self.bot = bot

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        update: "raw.types.UpdateManagedBot",
        users: dict,
    ) -> "ManagedBot":
        bot_user = users.get(update.bot_id)
        return ManagedBot(
            client=client,
            user_id=update.user_id,
            bot_id=update.bot_id,
            bot=types.User._parse(client, bot_user) if bot_user else None,
        )

    @staticmethod
    def _parse_action(
        client: "pyrogram.Client",
        bot_id: int,
        users: dict,
    ) -> "ManagedBot":
        bot_user = users.get(bot_id)
        return ManagedBot(
            client=client,
            user_id=0,
            bot_id=bot_id,
            bot=types.User._parse(client, bot_user) if bot_user else None,
        )
