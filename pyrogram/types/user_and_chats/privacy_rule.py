
from typing import List, Optional

from pyrogram import enums, raw, types

from ..object import Object


class PrivacyRule(Object):
    """A privacy rule.

    Parameters:
        type (:obj:`~pyrogram.enums.PrivacyRuleType`):
            Privacy rule type.

        users (List of :obj:`~pyrogram.types.User`, *optional*):
            List of users.

        chats (List of :obj:`~pyrogram.types.Chat`, *optional*):
            List of chats.
    """

    def __init__(
        self, *,
        type: "types.PrivacyRuleType",
        users: Optional[List["types.User"]] = None,
        chats: Optional[List["types.Chat"]] = None
    ):
        super().__init__(None)

        self.type = type
        self.users = users
        self.chats = chats

    @staticmethod
    def _parse(client, rule: "raw.base.PrivacyRule", users: dict, chats: dict) -> "PrivacyRule":
        return PrivacyRule(
            type=enums.PrivacyRuleType(type(rule)),
            users=types.List(types.User._parse(client, users.get(i)) for i in getattr(rule, "users", [])) or None,
            chats=types.List(types.Chat._parse_chat(client, chats.get(i)) for i in getattr(rule, "chats", [])) or None
        )
