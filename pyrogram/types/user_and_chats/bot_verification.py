
from typing import Optional

from pyrogram import raw, types
from ..object import Object

class BotVerification(Object):
    """Information about bot verification.


    Parameters:
        bot (:obj:`~pyrogram.types.User`):
            Bot that is verified this user.

        custom_emoji_id (``int``):
            Custom emoji icon identifier.

        description (``int``, *optional*):
            Additional description about the verification.
    """

    def __init__(
        self,
        *,
        bot: int,
        custom_emoji_id: int,
        description: str
    ):
        self.bot = bot
        self.custom_emoji_id = custom_emoji_id
        self.description = description

    @staticmethod
    def _parse(
        client,
        verification: "raw.types.BotVerification",
        users
    ) -> Optional["BotVerification"]:
        if not verification:
            return None

        return BotVerification(
            bot=types.User._parse(client, users.get(verification.bot_id)),
            custom_emoji_id=verification.icon,
            description=verification.description
        )
