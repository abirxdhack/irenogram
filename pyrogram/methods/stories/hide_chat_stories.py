
from typing import Union

import pyrogram
from pyrogram import raw


class HideChatStories:
    async def hide_chat_stories(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
    ) -> bool:
        """Hide the active stories of a user, preventing them from being displayed on the action bar on the homescreen.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

        Returns:
            ``bool``: On success, a bool is returned.

        Example:
            .. code-block:: python

                await app.hide_chat_stories(chat_id)
        """
        r = await self.invoke(
            raw.functions.stories.TogglePeerStoriesHidden(
                peer=await self.resolve_peer(chat_id),
                hidden=True
            )
        )

        return r
