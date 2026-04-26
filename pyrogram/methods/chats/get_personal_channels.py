
from typing import List, Optional

import pyrogram
from pyrogram import raw, types


class GetPersonalChannels:
    async def get_personal_channels(
        self: "pyrogram.Client"
    ) -> Optional[List["types.Chat"]]:
        """Get all your public channels.

        .. include:: /_includes/usable-by/users.rst

        Returns:
            List of :obj:`~pyrogram.types.Chat`: On success, a list of personal channels is returned.

        Example:
            .. code-block:: python

                await app.get_personal_channels()
        """
        r = await self.invoke(
            raw.functions.channels.GetAdminedPublicChannels(
                for_personal=True
            )
        )

        return types.List(types.Chat._parse_chat(self, i) for i in r.chats) or None
