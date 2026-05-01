import os
import re
from datetime import datetime
from typing import Union, BinaryIO, List, Optional, Callable

import pyrogram
from pyrogram import StopTransmission, enums
from pyrogram import raw
from pyrogram import types
from pyrogram import utils
from pyrogram.errors import FilePartMissing
from pyrogram.file_id import FileType


class SendDocument:
    async def send_document(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        document: Union[str, BinaryIO],
        thumb: Union[str, BinaryIO] = None,
        caption: str = "",
        parse_mode: Optional["enums.ParseMode"] = None,
        caption_entities: List["types.MessageEntity"] = None,
        file_name: str = None,
        force_document: bool = None,
        disable_notification: bool = None,
        message_thread_id: int = None,
        business_connection_id: str = None,
        reply_to_message_id: int = None,
        reply_to_story_id: int = None,
        reply_to_chat_id: Union[int, str] = None,
        reply_to_monoforum_id: Union[int, str] = None,
        quote_text: str = None,
        quote_entities: List["types.MessageEntity"] = None,
        message_effect_id: int = None,
        schedule_date: datetime = None,
        protect_content: bool = None,
        allow_paid_broadcast: bool = None,
        reply_markup: Union[
            "types.InlineKeyboardMarkup",
            "types.ReplyKeyboardMarkup",
            "types.ReplyKeyboardRemove",
            "types.ForceReply"
        ] = None,
        progress: Callable = None,
        progress_args: tuple = ()
    ) -> Optional["types.Message"]:
        """Send generic files.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).
                You can also use chat public link in form of *t.me/<username>* (str).

            document (``str`` | ``BinaryIO``):
                File to send.
                Pass a file_id as string to send a file that exists on the Telegram servers,
                pass an HTTP URL as a string for Telegram to get a file from the Internet,
                pass a file path as string to upload a new file that exists on your local machine, or
                pass a binary file-like object with its attribute ".name" set for in-memory uploads.

            thumb (``str`` | ``BinaryIO``, *optional*):
                Thumbnail of the file sent.
                The thumbnail should be in JPEG format and less than 200 KB in size.
                A thumbnail's width and height should not exceed 320 pixels.
                Thumbnails can't be reused and can be only uploaded as a new file.

            caption (``str``, *optional*):
                Document caption, 0-1024 characters.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.

            caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
                List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

            file_name (``str``, *optional*):
                File name of the document sent.
                Defaults to file's path basename.

            force_document (``bool``, *optional*):
                Pass True to force sending files as document.

            disable_notification (``bool``, *optional*):
                Sends the message silently.

            message_thread_id (``int``, *optional*):
                Unique identifier for the target message thread.

            business_connection_id (``str``, *optional*):
                Business connection identifier.

            reply_to_message_id (``int``, *optional*):
                If the message is a reply, ID of the original message.

            reply_to_story_id (``int``, *optional*):
                Unique identifier for the target story.

            reply_to_chat_id (``int`` | ``str``, *optional*):
                Unique identifier for the origin chat.

            reply_to_monoforum_id (``int`` | ``str``, *optional*):
                Unique identifier for the target user of monoforum.

            quote_text (``str``, *optional*):
                Text to quote.

            quote_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
                Entities in quote_text.

            message_effect_id (``int`` ``64-bit``, *optional*):
                Message effect id.

            schedule_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the message will be sent.

            protect_content (``bool``, *optional*):
                Protects content.

            allow_paid_broadcast (``bool``, *optional*):
                Ignore broadcast limits.

            reply_markup:
                Reply markup.

            progress:
                Progress callback.

            progress_args:
                Extra args.

        Returns:
            :obj:`~pyrogram.types.Message` | ``None``
        """
        file = None

        reply_to = await utils.get_reply_to(
            client=self,
            chat_id=chat_id,
            reply_to_message_id=reply_to_message_id,
            reply_to_story_id=reply_to_story_id,
            message_thread_id=message_thread_id,
            reply_to_chat_id=reply_to_chat_id,
            reply_to_monoforum_id=reply_to_monoforum_id,
            quote_text=quote_text,
            quote_entities=quote_entities,
            parse_mode=parse_mode
        )

        try:
            if isinstance(document, str):
                if os.path.isfile(document):
                    thumb = await self.save_file(thumb)
                    file = await self.save_file(document, progress=progress, progress_args=progress_args)
                    media = raw.types.InputMediaUploadedDocument(
                        mime_type=self.guess_mime_type(document) or "application/zip",
                        file=file,
                        force_file=force_document or None,
                        thumb=thumb,
                        attributes=[
                            raw.types.DocumentAttributeFilename(file_name=file_name or os.path.basename(document))
                        ]
                    )
                elif re.match("^https?://", document):
                    media = raw.types.InputMediaDocumentExternal(url=document)
                else:
                    media = utils.get_input_media_from_file_id(document, FileType.DOCUMENT)
            else:
                thumb = await self.save_file(thumb)
                file = await self.save_file(document, progress=progress, progress_args=progress_args)
                media = raw.types.InputMediaUploadedDocument(
                    mime_type=self.guess_mime_type(file_name or document.name) or "application/zip",
                    file=file,
                    thumb=thumb,
                    attributes=[
                        raw.types.DocumentAttributeFilename(file_name=file_name or document.name)
                    ]
                )

            while True:
                try:
                    rpc = raw.functions.messages.SendMedia(
                        peer=await self.resolve_peer(chat_id),
                        media=media,
                        silent=disable_notification or None,
                        reply_to=reply_to,
                        random_id=self.rnd_id(),
                        schedule_date=utils.datetime_to_timestamp(schedule_date),
                        noforwards=protect_content,
                        allow_paid_floodskip=allow_paid_broadcast,
                        effect=message_effect_id,
                        reply_markup=await reply_markup.write(self) if reply_markup else None,
                        **await utils.parse_text_entities(self, caption, parse_mode, caption_entities)
                    )

                    r = await self.invoke(rpc)

                except FilePartMissing as e:
                    await self.save_file(document, file_id=file.id, file_part=e.value)
                else:
                    for i in r.updates:
                        if isinstance(i, (
                            raw.types.UpdateNewMessage,
                            raw.types.UpdateNewChannelMessage,
                            raw.types.UpdateNewScheduledMessage,
                            raw.types.UpdateBotNewBusinessMessage
                        )):
                            return await types.Message._parse(
                                self,
                                i.message,
                                {u.id: u for u in r.users},
                                {c.id: c for c in r.chats},
                                is_scheduled=isinstance(i, raw.types.UpdateNewScheduledMessage),
                                business_connection_id=business_connection_id
                            )
        except StopTransmission:
            return None
