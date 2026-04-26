
from typing import Union

import pyrogram
from pyrogram import raw, types

class GetChatSettings:
    async def get_chat_settings(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
    ) -> "types.ChatSettings":
        """Get the settings (peer settings) of a chat or user.

        Settings include flags such as whether you can report the peer for
        spam, add them as a contact, whether the chat was auto-archived, etc.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username of the target chat/user.

        Returns:
            :obj:`~pyrogram.types.ChatSettings`: On success.

        Raises:
            :raises ValueError: If the peer cannot be resolved (not joined / invalid).

        Example:
            .. code-block:: python

                settings = await app.get_chat_settings("me")
                print(settings.add_contact, settings.report_spam)
        """
        try:
            peer = await self.resolve_peer(chat_id)
        except Exception as e:
            raise ValueError(f"Cannot resolve peer for chat_id={chat_id!r}: {e}") from e

        result = await self.invoke(
            raw.functions.messages.GetPeerSettings(peer=peer)
        )

        return types.ChatSettings._parse(result)
