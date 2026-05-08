from datetime import datetime
from typing import Union, List, Iterable

import pyrogram
from pyrogram import raw, utils
from pyrogram import types

class ForwardMessages:
    async def forward_messages(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_ids: Union[int, Iterable[int]],
        message_thread_id: int = None,
        disable_notification: bool = None,
        schedule_date: datetime = None,
        repeat_period: int = None,
        hide_sender_name: bool = None,
        hide_captions: bool = None,
        protect_content: bool = None,
        allow_paid_broadcast: bool = None,
        video_start_timestamp: int = None,
        reply_parameters: "types.ReplyParameters" = None,
        paid_message_star_count: int = None
    ) -> Union["types.Message", List["types.Message"]]:
        """Forward messages of any kind.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            from_chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the source chat where the original message was sent.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            message_ids (``int`` | Iterable of ``int``):
                An iterable of message identifiers in the chat specified in *from_chat_id* or a single message id.

            message_thread_id (``int``, *optional*):
                Unique identifier of a message thread to which the message belongs.
                For supergroups only.

            disable_notification (``bool``, *optional*):
                Sends the message silently.
                Users will receive a notification with no sound.

            schedule_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the message will be automatically sent.

            repeat_period (``int``, *optional*):
                Period after which the message will be sent again in seconds.

            hide_sender_name (``bool``, *optional*):
                If True, the original author of the message will not be shown.

            hide_captions (``bool``, *optional*):
                If True, the original media captions will be removed.

            protect_content (``bool``, *optional*):
                Protects the contents of the sent message from forwarding and saving.

            allow_paid_broadcast (``bool``, *optional*):
                Pass True to allow the message to ignore regular broadcast limits for a small fee; for bots only.

            video_start_timestamp (``int``, *optional*):
                The new video start timestamp in milliseconds.

            reply_parameters (:obj:`~pyrogram.types.ReplyParameters`, *optional*):
                Describes reply parameters for the message that is being sent.

            paid_message_star_count (``int``, *optional*):
                The number of Telegram Stars that must be paid to buy access to the message.

        Returns:
            :obj:`~pyrogram.types.Message` | List of :obj:`~pyrogram.types.Message`: In case *message_ids* was not
            a list, a single message is returned, otherwise a list of messages is returned.

        Example:
            .. code-block:: python


                await app.forward_messages(to_chat, from_chat, 123)


                await app.forward_messages(to_chat, from_chat, [1, 2, 3])
        """

        is_iterable = not isinstance(message_ids, int)
        message_ids = list(message_ids) if is_iterable else [message_ids]

        r = await self.invoke(
            raw.functions.messages.ForwardMessages(
                to_peer=await self.resolve_peer(chat_id),
                from_peer=await self.resolve_peer(from_chat_id),
                id=message_ids,
                silent=disable_notification or None,
                random_id=[self.rnd_id() for _ in message_ids],
                schedule_date=utils.datetime_to_timestamp(schedule_date),
                schedule_repeat_period=repeat_period,
                drop_author=hide_sender_name,
                drop_media_captions=hide_captions,
                noforwards=protect_content,
                allow_paid_floodskip=allow_paid_broadcast,
                top_msg_id=message_thread_id,
                reply_to=await utils.get_reply_to(
                    self,
                    reply_parameters,
                    message_thread_id
                ),
                video_timestamp=video_start_timestamp,
                allow_paid_stars=paid_message_star_count
            )
        )

        messages = await utils.parse_messages(client=self, messages=r)

        return messages if is_iterable else messages[0] if messages else None