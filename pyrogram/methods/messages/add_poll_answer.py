
from typing import Union, Optional

import pyrogram
from pyrogram import raw, types, utils

class AddPollAnswer:
    async def add_poll_answer(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int,
        text: str,
        text_entities: Optional[list] = None,
        parse_mode: Optional["pyrogram.enums.ParseMode"] = None,
    ) -> "types.Message":
        """Dynamically add a new answer option to an open poll that supports user-added answers.

        This feature is part of Bot API 9.6 poll revolution — only works on polls
        where ``open_answers`` was set to True during creation.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            message_id (``int``):
                Identifier of the message containing the poll.

            text (``str``):
                Text of the new answer option to add (1-100 characters).

            text_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
                Special entities in the answer text.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                Parse mode for the text.

        Returns:
            :obj:`~pyrogram.types.Message`: On success, the updated poll message is returned.

        Example:
            .. code-block:: python

                await app.add_poll_answer(chat_id, message_id, "A new option")
        """
        option_text, option_entities = (
            await utils.parse_text_entities(self, text, parse_mode, text_entities)
        ).values()

        answer = raw.types.PollAnswer(
            text=raw.types.TextWithEntities(
                text=option_text,
                entities=option_entities or [],
            ),
            option=b"\x00",
        )

        r = await self.invoke(
            raw.functions.messages.AddPollAnswer(
                peer=await self.resolve_peer(chat_id),
                msg_id=message_id,
                answer=answer,
            )
        )

        for update in r.updates:
            if isinstance(
                update,
                (
                    raw.types.UpdateNewMessage,
                    raw.types.UpdateNewChannelMessage,
                    raw.types.UpdateEditMessage,
                    raw.types.UpdateEditChannelMessage,
                ),
            ):
                return await types.Message._parse(
                    self,
                    update.message,
                    {u.id: u for u in r.users},
                    {c.id: c for c in r.chats},
                )

        return None
