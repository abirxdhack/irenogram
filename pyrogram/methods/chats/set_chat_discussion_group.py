
from typing import Optional, Union

import pyrogram
from pyrogram import raw


class SetChatDiscussionGroup:
    async def set_chat_discussion_group(
        self: "pyrogram.Client", *,
        chat_id: Optional[Union[int, str]] = None,
        discussion_chat_id: Optional[Union[int, str]] = None
    ) -> bool:
        """Change the discussion group of a channel chat.

        Requires `can_change_info` administrator right in the channel if it is specified.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``, *optional*):
                Unique identifier (int) or username (str) of the target chat.
                Pass None to remove a link from the supergroup passed in the second argument to a linked channel chat (requires `can_pin_messages` member right in the supergroup)

            discussion_chat_id (``int`` | ``str``, *optional*):
                Unique identifier (int) or username (str) of a new channel's discussion group.
                Use the method :meth:`get_suitable_discussion_chats` to find all suitable groups.
                Pass None to remove the discussion group.

        Returns:
            ``bool``: True on success.

        Raises:
            :raises ValueError: In case a chat id or discussion chat id belongs to a user.

        Example:
            .. code-block:: python

                await app.set_chat_discussion_group(chat_id="@pyrogram", discussion_chat_id="@pyrogramchat")

                await app.set_chat_discussion_group(chat_id="@pyrogram")

                await app.set_chat_discussion_group(discussion_chat_id="@pyrogramchat")
        """
        if chat_id is None and discussion_chat_id is None:
            raise ValueError("At least one of 'chat_id' or 'discussion_chat_id' must be provided.")

        if chat_id is None:
            channel_peer = raw.types.InputChannelEmpty()
        else:
            channel_peer = await self.resolve_peer(chat_id)

            if not isinstance(channel_peer, raw.types.InputPeerChannel):
                raise ValueError(f'The chat_id "{chat_id}" does not belong to a channel')

        if discussion_chat_id is None:
            discussion_peer = raw.types.InputChannelEmpty()
        else:
            discussion_peer = await self.resolve_peer(discussion_chat_id)

            if not isinstance(discussion_peer, raw.types.InputPeerChannel):
                raise ValueError(f'The discussion_chat_id "{discussion_chat_id}" does not belong to a chat')

        return bool(
            await self.invoke(
                raw.functions.channels.SetDiscussionGroup(
                    broadcast=channel_peer,
                    group=discussion_peer
                )
            )
        )
