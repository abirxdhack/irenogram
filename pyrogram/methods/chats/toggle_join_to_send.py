
from typing import Union

import pyrogram
from pyrogram import raw
from pyrogram import errors


class ToggleJoinToSend:
    async def toggle_join_to_send(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        enabled: bool = False
    ) -> bool:
        """Enable or disable guest users' ability to send messages in a supergroup.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            enabled (``bool``):
                The new status. Pass True to enable guest users to send message.

        Returns:
            ``bool``: True on success. False otherwise.

        Example:
            .. code-block:: python

                await app.toggle_join_to_send()

                await app.toggle_join_to_send(enabled=True)
        """
        try:
            r = await self.invoke(
                raw.functions.channels.ToggleJoinToSend(
                    channel=await self.resolve_peer(chat_id),
                    enabled=enabled
                )
            )

            return bool(r)
        except errors.RPCError:
            return False
