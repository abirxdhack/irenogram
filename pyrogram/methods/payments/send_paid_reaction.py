
from typing import Union

import pyrogram
from pyrogram import raw, types

class SendPaidReaction:
    async def send_paid_reaction(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int,
        amount: int,
        anonymous: bool = None
    ) -> "types.MessageReactions":
        """Use this method to send paid reactions on a channel message.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                You can also use chat public link in form of *t.me/<username>* (str).

            message_id (``int``):
                Identifier of the target message. If the message belongs to a media group, the reaction is set to the first non-deleted message in the group instead.

            amount (``int``):
                Amount of stars to send.

            anonymous (``bool``, *optional*):
                Pass True to hide yourself from top senders list.

        Returns:
            :obj:`~pyrogram.types.MessageReactions`: On success, MessageReactions is returned.

        Example:
            .. code-block:: python


                await app.send_paid_reaction(chat_id, message_id=message_id, amount=5)
        """
        r = await self.invoke(
            raw.functions.messages.SendPaidReaction(
                peer=await self.resolve_peer(chat_id),
                msg_id=message_id,
                count=amount,
                random_id=self.rnd_id(),
                private=anonymous
            )
        )
        users = {i.id: i for i in r.users}
        chats = {i.id: i for i in r.chats}

        for i in r.updates:
            if isinstance(i, raw.types.UpdateMessageReactions):
                return types.MessageReactions._parse(self, i.reactions, users, chats)
