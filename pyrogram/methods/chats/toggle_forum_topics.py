
from typing import Union

import pyrogram
from pyrogram import errors, raw


class ToggleForumTopics:
    async def toggle_forum_topics(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        is_forum: bool = False,
        has_forum_tabs: bool = False
    ) -> bool:
        """Enable or disable forum functionality in a supergroup.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            is_forum (``bool``):
                The new status.
                Pass True to enable forum topics.
                Defaults to False.

            has_forum_tabs (``bool``):
                Whether to enable or disable tabs in the forum.
                Defaults to False.

        Returns:
            ``bool``: True on success. False otherwise.

        Example:
            .. code-block:: python

                await app.toggle_forum_topics(is_forum=False)

                await app.toggle_forum_topics(is_forum=True)
        """
        try:
            r = await self.invoke(
                raw.functions.channels.ToggleForum(
                    channel=await self.resolve_peer(chat_id),
                    enabled=is_forum,
                    tabs=has_forum_tabs
                )
            )

            return bool(r)
        except errors.RPCError:
            return False
