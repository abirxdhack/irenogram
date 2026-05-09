from typing import List, Optional

from pyrogram import raw, types

from ..object import Object


class BotAccessSettings(Object):
    """This object describes the access settings of a bot.

    Parameters:
        is_access_restricted (``bool``):
            True if only selected users can access the bot. The bot's owner can always access it.

        added_users (List of :obj:`~pyrogram.types.User`, *optional*):
            The list of other users who have access to the bot if the access is restricted.
    """

    def __init__(
        self,
        *,
        is_access_restricted: bool,
        added_users: Optional[List["types.User"]] = None,
    ):
        super().__init__()

        self.is_access_restricted = is_access_restricted
        self.added_users = added_users

    @staticmethod
    def _parse(client, bot_access_settings: "raw.base.bots.AccessSettings"):
        return BotAccessSettings(
            is_access_restricted=bot_access_settings.access_restricted,
            added_users=types.List(
                [types.User._parse(client, i) for i in bot_access_settings.add_users]
            )
            if bot_access_settings.add_users
            else None,
        )