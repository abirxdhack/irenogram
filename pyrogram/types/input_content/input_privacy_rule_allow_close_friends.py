
import pyrogram
from pyrogram import raw
from .input_privacy_rule import InputPrivacyRule


class InputPrivacyRuleAllowCloseFriends(InputPrivacyRule):
    """Allow only close friends."""

    def __init__(
        self,
    ):
        super().__init__()

    async def write(self, client: "pyrogram.Client"):
        return raw.types.InputPrivacyValueAllowCloseFriends()
