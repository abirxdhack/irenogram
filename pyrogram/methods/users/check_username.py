
from typing import Union

import pyrogram
from pyrogram import raw


class CheckUsername:
    async def check_username(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        username: str
    ) -> bool:
        """Check if a username is available.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            username (``str``):
                Username to check.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.check_username("me", "username")
        """
        peer = await self.resolve_peer(chat_id)

        if isinstance(peer, raw.types.InputPeerChannel):
            r = await self.invoke(
                raw.functions.channels.CheckUsername(
                    channel=peer,
                    username=username
                )
            )
        else:
            r = await self.invoke(
                raw.functions.account.CheckUsername(
                    username=username
                )
            )

        return bool(r)
