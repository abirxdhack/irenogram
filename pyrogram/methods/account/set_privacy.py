
from typing import List, Union

import pyrogram
from pyrogram import raw, types, enums


class SetPrivacy:
    async def set_privacy(
        self: "pyrogram.Client",
        key: "enums.PrivacyKey",
        rules: List[Union[
            "types.InputPrivacyRuleAllowAll",
            "types.InputPrivacyRuleAllowBots",
            "types.InputPrivacyRuleAllowChats",
            "types.InputPrivacyRuleAllowCloseFriends",
            "types.InputPrivacyRuleAllowContacts",
            "types.InputPrivacyRuleAllowPremium",
            "types.InputPrivacyRuleAllowUsers",
            "types.InputPrivacyRuleDisallowAll",
            "types.InputPrivacyRuleDisallowBots",
            "types.InputPrivacyRuleDisallowChats",
            "types.InputPrivacyRuleDisallowContacts",
            "types.InputPrivacyRuleDisallowUsers"
        ]],
    ):
        """Set account privacy rules.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            key (:obj:`~pyrogram.enums.PrivacyKey`):
                Privacy key.

            rules (Iterable of :obj:`~pyrogram.types.InputPrivacyRule`):
                List of privacy rules.

        Returns:
            List of :obj:`~pyrogram.types.PrivacyRule`: On success, the list of privacy rules is returned.

        Example:
            .. code-block:: python

                from pyrogram import enums, types

                await app.set_privacy(enums.PrivacyKey.PHONE_NUMBER, [types.InputPrivacyRuleDisallowAll()])
        """
        r = await self.invoke(
            raw.functions.account.SetPrivacy(
                key=key.value(),
                rules=[await rule.write(self) for rule in rules]
            )
        )

        users = {i.id: i for i in r.users}
        chats = {i.id: i for i in r.chats}

        return types.List(types.PrivacyRule._parse(self, rule, users, chats) for rule in r.rules)
