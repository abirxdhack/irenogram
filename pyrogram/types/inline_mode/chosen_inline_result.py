
from base64 import b64encode
from struct import pack
from typing import Optional, Union

import pyrogram
from pyrogram import raw, enums
from pyrogram import types
from ..object import Object
from ..update import Update

class ChosenInlineResult(Object, Update):
    """A :doc:`result <InlineQueryResult>` of an inline query chosen by the user and sent to their chat partner.

    .. note::

        In order to receive these updates, your bot must have "inline feedback" enabled. You can enable this feature
        with `@BotFather <https://t.me/botfather>`_.

    Parameters:
        result_id (``str``):
            The unique identifier for the result that was chosen.

        from_user (:obj:`~pyrogram.types.User`):
            The user that chose the result.

        query (``str``):
            The query that was used to obtain the result.

        location (:obj:`~pyrogram.types.Location`, *optional*):
            Sender location, only for bots that require user location.

        inline_message_id (``str``, *optional*):
            Identifier of the sent inline message.
            Available only if there is an :doc:`inline keyboard <InlineKeyboardMarkup>` attached to the message.
            Will be also received in :doc:`callback queries <CallbackQuery>` and can be used to edit the message.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        result_id: str,
        from_user: "types.User",
        query: str,
        location: "types.Location" = None,
        inline_message_id: str = None
    ):
        super().__init__(client)

        self.result_id = result_id
        self.from_user = from_user
        self.query = query
        self.location = location
        self.inline_message_id = inline_message_id

    @staticmethod
    def _parse(client, chosen_inline_result: raw.types.UpdateBotInlineSend, users) -> "ChosenInlineResult":
        inline_message_id = None

        if isinstance(chosen_inline_result.msg_id, raw.types.InputBotInlineMessageID):
            inline_message_id = b64encode(
                pack(
                    "<iqq",
                    chosen_inline_result.msg_id.dc_id,
                    chosen_inline_result.msg_id.id,
                    chosen_inline_result.msg_id.access_hash
                ),
                b"-_"
            ).decode().rstrip("=")

        return ChosenInlineResult(
            result_id=str(chosen_inline_result.id),
            from_user=types.User._parse(client, users[chosen_inline_result.user_id]),
            query=chosen_inline_result.query,
            location=types.Location(
                longitude=chosen_inline_result.geo.long,
                latitude=chosen_inline_result.geo.lat,
                client=client
            ) if chosen_inline_result.geo else None,
            inline_message_id=inline_message_id
        )

    async def edit_message_text(
        self,
        text: str,
        parse_mode: Optional["enums.ParseMode"] = None,
        link_preview_options: "types.LinkPreviewOptions" = None,
        reply_markup: "types.InlineKeyboardMarkup" = None
    ) -> Union["types.Message", bool]:
        """Bound method *edit_message_text* of :obj:`~pyrogram.types.ChosenInlineResult`.

        Use as a shortcut for:

        .. code-block:: python

            await client.edit_inline_text(
                inline_message_id=inline_message_id,
                text=text
            )

        Example:
            .. code-block:: python

               await chosen_inline_result.edit_message_text("new text")

        Parameters:
            text (``str``):
                New text of the message.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.

            link_preview_options (:obj:`~pyrogram.types.LinkPreviewOptions`, *optional*):
                Options for link preview generation.

            reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
                An InlineKeyboardMarkup object.

        Returns:
            :obj:`~pyrogram.types.Message` | ``bool``: On success, the edited message or True.
        """
        return await self._client.edit_inline_text(
            inline_message_id=self.inline_message_id,
            text=text,
            parse_mode=parse_mode,
            link_preview_options=link_preview_options,
            reply_markup=reply_markup
        )

    async def edit_message_caption(
        self,
        caption: str,
        parse_mode: Optional["enums.ParseMode"] = None,
        reply_markup: "types.InlineKeyboardMarkup" = None
    ) -> Union["types.Message", bool]:
        """Bound method *edit_message_caption* of :obj:`~pyrogram.types.ChosenInlineResult`.

        Use as a shortcut for:

        .. code-block:: python

            await client.edit_inline_caption(
                inline_message_id=inline_message_id,
                caption=caption
            )

        Example:
            .. code-block:: python

               await chosen_inline_result.edit_message_caption("new caption")

        Parameters:
            caption (``str``):
                New caption of the message.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.

            reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
                An InlineKeyboardMarkup object.

        Returns:
            :obj:`~pyrogram.types.Message` | ``bool``: On success, the edited message or True.
        """
        return await self._client.edit_inline_caption(
            inline_message_id=self.inline_message_id,
            caption=caption,
            parse_mode=parse_mode,
            reply_markup=reply_markup
        )

    async def edit_message_media(
        self,
        media: "types.InputMedia",
        reply_markup: "types.InlineKeyboardMarkup" = None
    ) -> Union["types.Message", bool]:
        """Bound method *edit_message_media* of :obj:`~pyrogram.types.ChosenInlineResult`.

        Use as a shortcut for:

        .. code-block:: python

            await client.edit_inline_media(
                inline_message_id=inline_message_id,
                media=media
            )

        Example:
            .. code-block:: python

               await chosen_inline_result.edit_message_media(media)

        Parameters:
            media (:obj:`~pyrogram.types.InputMedia`):
                One of the InputMedia objects describing the media to edit.

            reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
                An InlineKeyboardMarkup object.

        Returns:
            :obj:`~pyrogram.types.Message` | ``bool``: On success, the edited message or True.
        """
        return await self._client.edit_inline_media(
            inline_message_id=self.inline_message_id,
            media=media,
            reply_markup=reply_markup
        )

    async def edit_message_reply_markup(
        self,
        reply_markup: "types.InlineKeyboardMarkup" = None
    ) -> Union["types.Message", bool]:
        """Bound method *edit_message_reply_markup* of :obj:`~pyrogram.types.ChosenInlineResult`.

        Use as a shortcut for:

        .. code-block:: python

            await client.edit_inline_reply_markup(
                inline_message_id=inline_message_id,
                reply_markup=reply_markup
            )

        Example:
            .. code-block:: python

               await chosen_inline_result.edit_message_reply_markup(reply_markup)

        Parameters:
            reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
                An InlineKeyboardMarkup object.

        Returns:
            :obj:`~pyrogram.types.Message` | ``bool``: On success, the edited message or True.
        """
        return await self._client.edit_inline_reply_markup(
            inline_message_id=self.inline_message_id,
            reply_markup=reply_markup
        )
