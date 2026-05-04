
from datetime import datetime
from typing import Union, List, Optional, BinaryIO

import pyrogram
from pyrogram import enums, types, utils
from pyrogram.file_id import FileId


class Message(types.Object):
    """Represents a message."""

    async def copy(
        self,
        chat_id: Union[int, str],
        caption: Optional[str] = None,
        parse_mode: Optional["enums.ParseMode"] = None,
        caption_entities: List["types.MessageEntity"] = None,
        disable_notification: bool = None,
        message_thread_id: int = None,
        reply_to_message_id: int = None,
        reply_to_chat_id: Union[int, str] = None,
        schedule_date: datetime = None,
        protect_content: bool = None,
        has_spoiler: bool = None,
        show_caption_above_media: bool = None,
        business_connection_id: str = None,
        allow_paid_broadcast: bool = None,
        paid_message_star_count: int = None,
        reply_markup: Union[
            "types.InlineKeyboardMarkup",
            "types.ReplyKeyboardMarkup",
            "types.ReplyKeyboardRemove",
            "types.ForceReply"
        ] = None
    ) -> "types.Message":
        """Bound method *copy* of :obj:`~pyrogram.types.Message`.

        Use as a shortcut for:

        .. code-block:: python

            await client.copy_message(
                chat_id=chat_id,
                from_chat_id=message.chat.id,
                message_id=message.id,
                caption=caption,
                parse_mode=parse_mode,
                caption_entities=caption_entities,
                disable_notification=disable_notification,
                message_thread_id=message_thread_id,
                reply_to_message_id=reply_to_message_id,
                reply_to_chat_id=reply_to_chat_id,
                schedule_date=schedule_date,
                protect_content=protect_content,
                has_spoiler=has_spoiler,
                show_caption_above_media=show_caption_above_media,
                business_connection_id=business_connection_id,
                allow_paid_broadcast=allow_paid_broadcast,
                paid_message_star_count=paid_message_star_count,
                reply_markup=reply_markup
            )

        Example:
            .. code-block:: python

                await message.copy(chat_id)

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).
                You can also use chat public link in form of *t.me/<username>* (str).

            caption (``str``, *optional*):
                New caption for media, 0-1024 characters after entities parsing.
                If not specified, the original caption is kept.
                Pass "" (empty string) to remove the caption.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.

            caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
                List of special entities that appear in the new caption, which can be specified instead of *parse_mode*.

            disable_notification (``bool``, *optional*):
                Sends the message silently.
                Users will receive a notification with no sound.

            message_thread_id (``int``, *optional*):
                Unique identifier for the target message thread (topic) of the forum.
                For supergroups only.

            reply_to_message_id (``int``, *optional*):
                If the message is a reply, ID of the original message.

            reply_to_chat_id (``int`` | ``str``, *optional*):
                If the message is a reply, ID of the original chat.

            schedule_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the message will be automatically sent.

            protect_content (``bool``, *optional*):
                Protects the contents of the sent message from forwarding and saving.

            has_spoiler (``bool``, *optional*):
                True, if the message media is covered by a spoiler animation.

            show_caption_above_media (``bool``, *optional*):
                If True, caption must be shown above the message media.

            business_connection_id (``str``, *optional*):
                Unique identifier of the business connection on behalf of which the message will be sent.

            allow_paid_broadcast (``bool``, *optional*):
                If True, you will be allowed to send up to 1000 messages per second.
                Ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message.
                The relevant Stars will be withdrawn from the bot's balance.
                For bots only.

            paid_message_star_count (``int``, *optional*):
                The number of Telegram Stars the user agreed to pay to send the messages.

            reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
                Additional interface options. An object for an inline keyboard, custom reply keyboard,
                instructions to remove reply keyboard or to force a reply from the user.

        Returns:
            :obj:`~pyrogram.types.Message`: On success, the copied message is returned.

        Raises:
            :class:`~pyrogram.errors.RPCError`: In case of a Telegram RPC error.
        """
        return await self._client.copy_message(
            chat_id=chat_id,
            from_chat_id=self.chat.id,
            message_id=self.id,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            disable_notification=disable_notification,
            message_thread_id=message_thread_id,
            reply_to_message_id=reply_to_message_id,
            reply_to_chat_id=reply_to_chat_id,
            schedule_date=schedule_date,
            protect_content=protect_content,
            has_spoiler=has_spoiler,
            show_caption_above_media=show_caption_above_media,
            business_connection_id=business_connection_id,
            allow_paid_broadcast=allow_paid_broadcast,
            paid_message_star_count=paid_message_star_count,
            reply_markup=reply_markup
        )