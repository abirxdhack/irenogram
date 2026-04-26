
from typing import Union

import pyrogram
from pyrogram import raw


class GetChatAudiosCount:
    async def get_chat_audios_count(
        self: "pyrogram.Client",
        chat_id: Union[int, str]
    ) -> int:
        """Get the total count of audios for a chat.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

        Returns:
            ``int``: On success, the user profile audios count is returned.

        Example:
            .. code-block:: python

                count = await app.get_chat_audios_count("me")
                print(count)
        """

        peer_id = await self.resolve_peer(chat_id)

        r = await self.invoke(
            raw.functions.users.GetSavedMusic(
                id=peer_id,
                offset=0,
                limit=1,
                hash=0
            )
        )

        return r.count
