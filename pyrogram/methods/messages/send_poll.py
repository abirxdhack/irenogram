from datetime import datetime
from typing import Union, List, Optional

import pyrogram
from pyrogram import raw, utils
from pyrogram import types, enums


class SendPoll:
    async def send_poll(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        question: str,
        options: List["types.PollOption"],
        question_entities: List["types.MessageEntity"] = None,
        is_anonymous: bool = True,
        type: "enums.PollType" = enums.PollType.REGULAR,
        allows_multiple_answers: bool = None,
        correct_option_id: int = None,
        correct_option_ids: List[int] = None,
        explanation: str = None,
        explanation_parse_mode: "enums.ParseMode" = None,
        explanation_entities: List["types.MessageEntity"] = None,
        open_period: int = None,
        close_date: datetime = None,
        is_closed: bool = None,
        allows_revoting: bool = None,
        hide_results_until_close: bool = None,
        shuffle_answers: bool = None,
        open_answers: bool = None,
        reply_to_poll_option: bytes = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        allow_paid_broadcast: bool = None,
        message_thread_id: int = None,
        business_connection_id: str = None,
        reply_to_message_id: int = None,
        reply_to_chat_id: Union[int, str] = None,
        quote_text: str = None,
        quote_entities: List["types.MessageEntity"] = None,
        parse_mode: Optional["enums.ParseMode"] = None,
        schedule_date: datetime = None,
        message_effect_id: int = None,
        reply_markup: Union[
            "types.InlineKeyboardMarkup",
            "types.ReplyKeyboardMarkup",
            "types.ReplyKeyboardRemove",
            "types.ForceReply",
        ] = None,
    ) -> "types.Message":
        """Send a new poll.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).
                You can also use chat public link in form of *t.me/<username>* (str).

            question (``str``):
                Poll question, 1-255 characters.

            options (List of :obj:`~pyrogram.types.PollOption`):
                List of PollOption objects.

            question_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
                List of special entities that appear in the poll question.

            is_anonymous (``bool``, *optional*):
                True, if the poll needs to be anonymous.
                Defaults to True.

            type (:obj:`~pyrogram.enums.PollType`, *optional*):
                Poll type, QUIZ or REGULAR.
                Defaults to REGULAR.

            allows_multiple_answers (``bool``, *optional*):
                True, if the poll allows multiple answers, ignored for quiz polls.

            correct_option_id (``int``, *optional*):
                0-based identifier of the correct answer option for quiz polls.
                Deprecated in favor of correct_option_ids for multi-correct support.

            correct_option_ids (List of ``int``, *optional*):
                0-based identifiers of all correct answer options for quiz polls.
                Supports multiple correct answers (Bot API 9.6+).

            explanation (``str``, *optional*):
                Text shown when a user chooses an incorrect answer in a quiz poll, 0-200 characters.

            explanation_parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                Parse mode for the explanation text.

            explanation_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
                Entities in the explanation text.

            open_period (``int``, *optional*):
                Amount of time in seconds the poll will be active after creation, 5-600.

            close_date (:py:obj:`~datetime.datetime`, *optional*):
                Point in time when the poll will be automatically closed.

            is_closed (``bool``, *optional*):
                Pass True to immediately close the poll. Useful for poll preview.

            allows_revoting (``bool``, *optional*):
                Pass True to allow voters to change their vote (Bot API 9.6+).
                Pass False to disable revoting explicitly.

            hide_results_until_close (``bool``, *optional*):
                Pass True to hide poll results until the poll is closed (Bot API 9.6+).

            shuffle_answers (``bool``, *optional*):
                Pass True to shuffle answer options for each voter (Bot API 9.6+).

            open_answers (``bool``, *optional*):
                Pass True to allow users to add new answer options dynamically (Bot API 9.6+).

            reply_to_poll_option (``bytes``, *optional*):
                Option data bytes to reply to a specific poll option (Bot API 9.6+).

            disable_notification (``bool``, *optional*):
                Sends the message silently. Users will receive a notification with no sound.

            protect_content (``bool``, *optional*):
                Protects the contents of the sent message from forwarding and saving.

            allow_paid_broadcast (``bool``, *optional*):
                Pass True to allow the message to ignore regular broadcast limits for a small fee; for bots only.

            message_thread_id (``int``, *optional*):
                Unique identifier for the target message thread (topic) of the forum.

            business_connection_id (``str``, *optional*):
                Business connection identifier.

            reply_to_message_id (``int``, *optional*):
                If the message is a reply, ID of the original message.

            reply_to_chat_id (``int`` | ``str``, *optional*):
                Unique identifier for the origin chat for cross-chat replies.

            quote_text (``str``, *optional*):
                Text to quote for reply_to_message.

            quote_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
                Entities in the quote_text.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                Parse mode for the quote_text.

            schedule_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the message will be automatically sent.

            message_effect_id (``int`` ``64-bit``, *optional*):
                Unique identifier of the message effect to be added to the message.

            reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
                Additional interface options.

        Returns:
            :obj:`~pyrogram.types.Message`: On success, the sent poll message is returned.

        Example:
            .. code-block:: python

                from pyrogram.types import PollOption

                await app.send_poll(
                    chat_id,
                    "Is this a poll question?",
                    [
                        PollOption("Yes"),
                        PollOption("No"),
                        PollOption("Maybe"),
                    ]
                )
        """
        reply_to = await utils.get_reply_to(
            client=self,
            chat_id=chat_id,
            reply_to_message_id=reply_to_message_id,
            message_thread_id=message_thread_id,
            reply_to_chat_id=reply_to_chat_id,
            quote_text=quote_text,
            quote_entities=quote_entities,
            parse_mode=parse_mode,
        )

        if reply_to_poll_option is not None and reply_to is not None:
            if hasattr(reply_to, "poll_option"):
                reply_to.poll_option = reply_to_poll_option

        solution, solution_entities = (
            await utils.parse_text_entities(self, explanation, explanation_parse_mode, explanation_entities)
        ).values()

        q, q_entities = (
            await pyrogram.utils.parse_text_entities(self, question, None, question_entities)
        ).values()

        correct_answers_bytes = None
        if type == enums.PollType.QUIZ:
            if correct_option_ids is not None:
                correct_answers_bytes = [bytes([idx]) for idx in correct_option_ids]
            elif correct_option_id is not None:
                correct_answers_bytes = [bytes([correct_option_id])]

        revoting_disabled_flag = None
        if allows_revoting is not None:
            revoting_disabled_flag = not allows_revoting

        rpc = raw.functions.messages.SendMedia(
            peer=await self.resolve_peer(chat_id),
            media=raw.types.InputMediaPoll(
                poll=raw.types.Poll(
                    id=self.rnd_id(),
                    question=raw.types.TextWithEntities(text=q, entities=q_entities or []),
                    answers=[
                        await types.PollOption(text=option.text, entities=option.entities).write(self, i)
                        for i, option in enumerate(options)
                    ],
                    closed=is_closed,
                    public_voters=not is_anonymous,
                    multiple_choice=allows_multiple_answers,
                    quiz=type == enums.PollType.QUIZ or False,
                    open_answers=open_answers,
                    revoting_disabled=revoting_disabled_flag,
                    shuffle_answers=shuffle_answers,
                    hide_results_until_close=hide_results_until_close,
                    close_period=open_period,
                    close_date=utils.datetime_to_timestamp(close_date),
                    hash=0,
                ),
                correct_answers=correct_answers_bytes,
                solution=solution,
                solution_entities=solution_entities or [],
            ),
            message="",
            silent=disable_notification,
            reply_to=reply_to,
            random_id=self.rnd_id(),
            schedule_date=utils.datetime_to_timestamp(schedule_date),
            noforwards=protect_content,
            allow_paid_floodskip=allow_paid_broadcast,
            reply_markup=await reply_markup.write(self) if reply_markup else None,
            effect=message_effect_id,
        )

        if business_connection_id is not None:
            r = await self.invoke(
                raw.functions.InvokeWithBusinessConnection(
                    connection_id=business_connection_id,
                    query=rpc,
                )
            )
        else:
            r = await self.invoke(rpc)

        for i in r.updates:
            if isinstance(
                i,
                (
                    raw.types.UpdateNewMessage,
                    raw.types.UpdateNewChannelMessage,
                    raw.types.UpdateNewScheduledMessage,
                    raw.types.UpdateBotNewBusinessMessage,
                ),
            ):
                return await types.Message._parse(
                    self,
                    i.message,
                    {u.id: u for u in r.users},
                    {c.id: c for c in r.chats},
                    is_scheduled=isinstance(i, raw.types.UpdateNewScheduledMessage),
                    business_connection_id=business_connection_id,
                )
