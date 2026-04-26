
from typing import Union, Optional

import pyrogram
from pyrogram import raw


class SetPersonalChannel:
    async def set_personal_channel(
        self: "pyrogram.Client",
        chat_id: Optional[Union[int, str]] = None
    ) -> bool:
        """Set a personal channel in bio.

        .. include:: /_includes/usable-by/users.rst

        To get all available channels you can use
        :meth:`~pyrogram.Client.get_personal_channels`.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user or None to remove it.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.set_personal_channel(chat_id)

                await app.set_personal_channel()
        """
        if chat_id is None:
            peer = raw.types.InputChannelEmpty()
        else:
            peer = await self.resolve_peer(chat_id)

            if not isinstance(peer, raw.types.InputPeerChannel):
                return False

        return bool(
            await self.invoke(
                raw.functions.account.UpdatePersonalChannel(
                    channel=peer
                )
            )
        )
