
import pyrogram
from pyrogram import raw
from .input_privacy_rule import InputPrivacyRule


class InputPrivacyRuleDisallowBots(InputPrivacyRule):
    """Disallow bots and miniapps."""

    def __init__(
        self,
    ):
        super().__init__()

    async def write(self, client: "pyrogram.Client"):
        return raw.types.InputPrivacyValueDisallowBots()
