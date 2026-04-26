
from typing import Union

import pyrogram
from pyrogram import raw, types, utils


class SetChatTTL:
    async def set_chat_ttl(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        ttl_seconds: int
    ) -> "types.Message":
        """Set the time-to-live for the chat.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            ttl_seconds (``int``):
                The time-to-live for the chat.
                Either 86000 for 1 day, 604800 for 1 week or 0 (zero) to disable it.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.set_chat_ttl(chat_id, 86400)

                await app.set_chat_ttl(chat_id, 604800)

                await app.set_chat_ttl(chat_id, 0)
        """
        r = await self.invoke(
            raw.functions.messages.SetHistoryTTL(
                peer=await self.resolve_peer(chat_id),
                period=ttl_seconds,
            )
        )

        messages = await utils.parse_messages(client=self, messages=r)

        return messages[0] if messages else None
