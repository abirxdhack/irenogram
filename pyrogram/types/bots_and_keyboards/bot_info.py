
from pyrogram import raw

from ..object import Object

class BotInfo(Object):
    """A bot Information.


    Parameters:
        name (``str``):
            The bot name.

        about (``str``):
            The bot bio.

        description (``str``):
            Description of the bot;

        privacy_policy_url (``str``, *optional*):
            Privacy policy URL of the bot.
    """

    def __init__(self, name: str, about: str, description: str, privacy_policy_url: str = None):
        super().__init__()

        self.name = name
        self.about = about
        self.description = description
        self.privacy_policy_url = privacy_policy_url

    @staticmethod
    def _parse(bot_info: "raw.types.bots.BotInfo") -> "BotInfo":
        return BotInfo(
            name=getattr(bot_info,"name", None),
            about=getattr(bot_info,"about", None),
            description=getattr(bot_info,"description", None),
            privacy_policy_url=getattr(bot_info,"privacy_policy_url", None)
        )
