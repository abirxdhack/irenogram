from typing import Union, List, Optional

import pyrogram
from pyrogram import raw
from pyrogram import types


class VotePoll:
    async def vote_poll(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int,
        options: Union[int, List[int]],
        retract: bool = False,
    ) -> "types.Poll":
        """Vote in a poll or retract an existing vote.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).
                You can also use chat public link in form of *t.me/<username>* (str).

            message_id (``int``):
                Identifier of the original message with the poll.

            options (``int`` | List of ``int``):
                Index or list of indexes (for multiple answers) of the poll option(s) you want to vote for (0 to 9).
                Pass an empty list ``[]`` together with ``retract=True`` to retract your existing vote.

            retract (``bool``, *optional*):
                Pass True to retract the current vote without casting a new one.
                Requires that the poll has revoting enabled (Bot API 9.6+).
                Defaults to False.

        Returns:
            :obj:`~pyrogram.types.Poll` - On success, the updated poll is returned.

        Example:
            .. code-block:: python

                await app.vote_poll(chat_id, message_id, 6)

                await app.vote_poll(chat_id, message_id, [0, 2])

                await app.vote_poll(chat_id, message_id, [], retract=True)
        """
        poll_message = await self.get_messages(chat_id, message_id)
        poll = poll_message.poll

        if retract:
            chosen_options: List[bytes] = []
        else:
            option_indexes = [options] if not isinstance(options, list) else options
            chosen_options = [poll.options[idx].data for idx in option_indexes]

        r = await self.invoke(
            raw.functions.messages.SendVote(
                peer=await self.resolve_peer(chat_id),
                msg_id=message_id,
                options=chosen_options,
            )
        )

        for update in r.updates:
            if isinstance(update, raw.types.UpdateMessagePoll):
                return await types.Poll._parse_update(
                    self,
                    update,
                    {u.id: u for u in r.users},
                )

        if r.updates:
            return await types.Poll._parse(self, r.updates[0], {u.id: u for u in r.users})

        return poll
