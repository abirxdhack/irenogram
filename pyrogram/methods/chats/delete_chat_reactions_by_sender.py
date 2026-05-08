from typing import Union

import pyrogram
from pyrogram import raw


class DeleteChatReactionsBySender:
    async def delete_chat_reactions_by_sender(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        sender_id: Union[int, str],
    ) -> bool:
        """Delete all reactions sent by a certain user in a chat.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            sender_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the user whose reactions will be deleted.

        Returns:
            ``bool``: True on success, False otherwise.
        """

        return await self.invoke(
            raw.functions.messages.DeleteParticipantReactions(
                peer=await self.resolve_peer(chat_id),
                participant=await self.resolve_peer(sender_id),
            )
        )