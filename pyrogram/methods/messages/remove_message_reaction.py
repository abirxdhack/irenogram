from typing import Union

import pyrogram
from pyrogram import raw, types


class RemoveMessageReaction:
    async def remove_message_reaction(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int,
        sender_id: Union[int, str],
    ) -> "types.List":
        """Remove a specific reaction from a message by a particular user.

        Admins can remove individual reactions on messages within their chats.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            message_id (``int``):
                Identifier of the message from which the reaction should be removed.

            sender_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the user whose reaction will be removed.

        Returns:
            List of :obj:`~pyrogram.types.Message`: On success, a list of service messages describing the changes is returned.

        Example:
            .. code-block:: python

                await app.remove_message_reaction(chat_id="mychat", message_id=1, sender_id=123456789)
        """
        r = await self.invoke(
            raw.functions.messages.DeleteParticipantReaction(
                peer=await self.resolve_peer(chat_id),
                msg_id=message_id,
                participant=await self.resolve_peer(sender_id),
            )
        )

        return types.List(
            [
                await types.Message._parse(self, m, {u.id: u for u in r.users}, {c.id: c for c in r.chats})
                for m in getattr(r, "updates", [])
                if hasattr(m, "message")
            ]
        )
