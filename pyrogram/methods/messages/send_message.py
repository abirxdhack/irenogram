from datetime import datetime
from typing import Union, List, Optional

import pyrogram
from pyrogram import raw, utils, enums
from pyrogram import types

class SendMessage:
    async def send_message(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        text: str,
        parse_mode: Optional["enums.ParseMode"] = None,
        entities: List["types.MessageEntity"] = None,

        disable_web_page_preview: bool = None,

        link_preview_options: "types.LinkPreviewOptions" = None,
        disable_notification: bool = None,
        message_thread_id: int = None,
        business_connection_id: str = None,
        reply_to_message_id: int = None,
        reply_to_story_id: int = None,
        reply_to_chat_id: int = None,
        reply_to_monoforum_id: Union[int, str] = None,
        quote_text: str = None,
        quote_entities: List["types.MessageEntity"] = None,
        schedule_date: datetime = None,
        protect_content: bool = None,
        allow_paid_broadcast: bool = None,
        invert_media: bool = None,
        message_effect_id: int = None,
        reply_markup: Union[
            "types.InlineKeyboardMarkup",
            "types.ReplyKeyboardMarkup",
            "types.ReplyKeyboardRemove",
            "types.ForceReply"
        ] = None
    ) -> "types.Message":
        """Send text messages.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).
                You can also use chat public link in form of *t.me/<username>* (str).

            text (``str``):
                Text of the message to be sent.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.

            entities (List of :obj:`~pyrogram.types.MessageEntity`):
                List of special entities that appear in message text, which can be specified instead of *parse_mode*.

            disable_web_page_preview (``bool``, *optional*):
                Disables link previews for links in this message.
                Legacy parameter — use ``link_preview_options`` for full control.

            link_preview_options (:obj:`~pyrogram.types.LinkPreviewOptions`, *optional*):
                Bot API-style link preview options.  When set, takes precedence over
                ``disable_web_page_preview`` and ``invert_media``.

                - ``is_disabled=True`` disables the preview entirely.
                - ``url`` specifies a custom preview URL.
                - ``prefer_large_media`` / ``prefer_small_media`` control thumbnail size.
                - ``show_above_text=True`` places the preview above the message text.

            disable_notification (``bool``, *optional*):
                Sends the message silently.
                Users will receive a notification with no sound.

            message_thread_id (``int``, *optional*):
                Unique identifier for the target message thread (topic) of the forum.
                for forum supergroups only.

            business_connection_id (``str``, *optional*):
                Business connection identifier.
                for business bots only.

            reply_to_message_id (``int``, *optional*):
                If the message is a reply, ID of the original message.

            reply_to_story_id (``int``, *optional*):
                Unique identifier for the target story.

            reply_to_chat_id (``int`` | ``str``, *optional*):
                Unique identifier for the origin chat.
                for reply to message from another chat.
                You can also use chat public link in form of *t.me/<username>* (str).

            reply_to_monoforum_id (``int`` | ``str``, *optional*):
                Unique identifier for the target user of the monoforum.
                for reply to message from a monoforum.
                for channel administrators only.

            quote_text (``str``, *optional*):
                Text to quote.
                for reply_to_message only.

            quote_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
                List of special entities that appear in quote_text, which can be specified instead of *parse_mode*.
                for reply_to_message only.

            schedule_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the message will be automatically sent.

            protect_content (``bool``, *optional*):
                Protects the contents of the sent message from forwarding and saving.

            allow_paid_broadcast (``bool``, *optional*):
                Pass True to allow the message to ignore regular broadcast limits for a small fee; for bots only

            invert_media (``bool``, *optional*):
                Move web page preview to above the message.
                Superseded by ``link_preview_options.show_above_text`` when that is set.

            message_effect_id (``int`` ``64-bit``, *optional*):
                Unique identifier of the message effect to be added to the message; for private chats only.

            reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
                Additional interface options. An object for an inline keyboard, custom reply keyboard,
                instructions to remove reply keyboard or to force a reply from the user.

        Returns:
            :obj:`~pyrogram.types.Message`: On success, the sent text message is returned.

        Example:
            .. code-block:: python

                # Simple example
                await app.send_message("me", "Message sent with **Pyrogram**!")

                # Disable web page preview (legacy)
                await app.send_message("me", "https://abirxdhack.github.io/irenogram",
                    disable_web_page_preview=True)

                # Disable preview via link_preview_options
                from pyrogram.types import LinkPreviewOptions
                await app.send_message("me", "https://abirxdhack.github.io/irenogram",
                    link_preview_options=LinkPreviewOptions(is_disabled=True))

                # Force large preview image, placed above text
                await app.send_message("me", "https://abirxdhack.github.io/irenogram",
                    link_preview_options=LinkPreviewOptions(
                        prefer_large_media=True,
                        show_above_text=True
                    ))

                # Reply to a message using its id
                await app.send_message("me", "this is a reply", reply_to_message_id=123)
        """

        message, entities = (await utils.parse_text_entities(self, text, parse_mode, entities)).values()

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

        if link_preview_options is not None:
            _no_webpage = link_preview_options.is_disabled or None

            _invert_media = link_preview_options.show_above_text or invert_media
            _preview_url = link_preview_options.url
            _force_large = link_preview_options.prefer_large_media
            _force_small = link_preview_options.prefer_small_media
        else:

            _no_webpage = disable_web_page_preview or None
            _invert_media = invert_media
            _preview_url = None
            _force_large = None
            _force_small = None

        use_web_page_media = bool(_preview_url or _force_large or _force_small)

        if use_web_page_media:

            media = raw.types.InputMediaWebPage(
                url=_preview_url or "",
                force_large_media=_force_large,
                force_small_media=_force_small,
                optional=not bool(_preview_url),
            )
            rpc = raw.functions.messages.SendMedia(
                peer=await self.resolve_peer(chat_id),
                media=media,
                silent=disable_notification or None,
                reply_to=reply_to,
                random_id=self.rnd_id(),
                schedule_date=utils.datetime_to_timestamp(schedule_date),
                reply_markup=await reply_markup.write(self) if reply_markup else None,
                message=message,
                entities=entities,
                noforwards=protect_content,
                allow_paid_floodskip=allow_paid_broadcast,
                invert_media=_invert_media,
                effect=message_effect_id,
            )
        else:
            rpc = raw.functions.messages.SendMessage(
                peer=await self.resolve_peer(chat_id),
                no_webpage=_no_webpage,
                silent=disable_notification or None,
                reply_to=reply_to,
                random_id=self.rnd_id(),
                schedule_date=utils.datetime_to_timestamp(schedule_date),
                reply_markup=await reply_markup.write(self) if reply_markup else None,
                message=message,
                entities=entities,
                noforwards=protect_content,
                allow_paid_floodskip=allow_paid_broadcast,
                invert_media=_invert_media,
                effect=message_effect_id,
            )

        if business_connection_id is not None:
            r = await self.invoke(
                raw.functions.InvokeWithBusinessConnection(
                    connection_id=business_connection_id,
                    query=rpc
                )
            )
        else:
            r = await self.invoke(rpc)

        if isinstance(r, raw.types.UpdateShortSentMessage):
            peer = await self.resolve_peer(chat_id)

            peer_id = (
                peer.user_id
                if isinstance(peer, raw.types.InputPeerUser)
                else -peer.chat_id
            )

            return types.Message(
                id=r.id,
                chat=types.Chat(
                    id=peer_id,
                    type=enums.ChatType.PRIVATE,
                    client=self
                ),
                text=message,
                date=utils.timestamp_to_datetime(r.date),
                outgoing=r.out,
                reply_markup=reply_markup,
                entities=[
                    types.MessageEntity._parse(None, entity, {})
                    for entity in entities
                ] if entities else None,
                client=self
            )

        for i in r.updates:
            if isinstance(i, (raw.types.UpdateNewMessage,
                              raw.types.UpdateNewChannelMessage,
                              raw.types.UpdateNewScheduledMessage,
                              raw.types.UpdateBotNewBusinessMessage)):
                return await types.Message._parse(
                    self, i.message,
                    {i.id: i for i in r.users},
                    {i.id: i for i in r.chats},
                    is_scheduled=isinstance(i, raw.types.UpdateNewScheduledMessage),
                    business_connection_id=business_connection_id
                )
