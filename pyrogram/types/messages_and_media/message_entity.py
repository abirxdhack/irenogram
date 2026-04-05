from typing import Optional, Dict

import pyrogram
from pyrogram import raw, enums
from pyrogram import types
from ..object import Object


class MessageEntity(Object):
    """One special entity in a text message.

    For example, hashtags, usernames, URLs, etc.

    Parameters:
        type (:obj:`~pyrogram.enums.MessageEntityType`):
            Type of the entity.

        offset (``int``):
            Offset in UTF-16 code units to the start of the entity.

        length (``int``):
            Length of the entity in UTF-16 code units.

        url (``str``, *optional*):
            For :obj:`~pyrogram.enums.MessageEntityType.TEXT_LINK` only, url that will be opened after user taps on the text.

        user (:obj:`~pyrogram.types.User`, *optional*):
            For :obj:`~pyrogram.enums.MessageEntityType.TEXT_MENTION` only, the mentioned user.

        language (``str``, *optional*):
            For ``pre`` only, the programming language of the entity text.

        custom_emoji_id (``int``, *optional*):
            For :obj:`~pyrogram.enums.MessageEntityType.CUSTOM_EMOJI` only, unique identifier of the custom emoji.
            Use :meth:`~pyrogram.Client.get_custom_emoji_stickers` to get full information about the sticker.

        collapsed (``bool``, *optional*):
            For :obj:`~pyrogram.enums.MessageEntityType.BLOCKQUOTE` only, whether the blockquote is expandable.

        date (``int``, *optional*):
            For :obj:`~pyrogram.enums.MessageEntityType.FORMATTED_DATE` only, the Unix timestamp of the date/time.

        relative (``bool``, *optional*):
            For :obj:`~pyrogram.enums.MessageEntityType.FORMATTED_DATE` only, show as relative time.

        short_time (``bool``, *optional*):
            For :obj:`~pyrogram.enums.MessageEntityType.FORMATTED_DATE` only, use short time format.

        long_time (``bool``, *optional*):
            For :obj:`~pyrogram.enums.MessageEntityType.FORMATTED_DATE` only, use long time format.

        short_date (``bool``, *optional*):
            For :obj:`~pyrogram.enums.MessageEntityType.FORMATTED_DATE` only, use short date format.

        long_date (``bool``, *optional*):
            For :obj:`~pyrogram.enums.MessageEntityType.FORMATTED_DATE` only, use long date format.

        day_of_week (``bool``, *optional*):
            For :obj:`~pyrogram.enums.MessageEntityType.FORMATTED_DATE` only, include day of week.

        old_text (``str``, *optional*):
            For :obj:`~pyrogram.enums.MessageEntityType.DIFF_REPLACE` only, the original text before replacement.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        type: "enums.MessageEntityType",
        offset: int,
        length: int,
        url: str = None,
        user: "types.User" = None,
        language: str = None,
        custom_emoji_id: int = None,
        collapsed: bool = None,
        date: int = None,
        relative: bool = None,
        short_time: bool = None,
        long_time: bool = None,
        short_date: bool = None,
        long_date: bool = None,
        day_of_week: bool = None,
        old_text: str = None,
    ):
        super().__init__(client)

        self.type = type
        self.offset = offset
        self.length = length
        self.url = url
        self.user = user
        self.language = language
        self.custom_emoji_id = custom_emoji_id
        self.collapsed = collapsed
        self.date = date
        self.relative = relative
        self.short_time = short_time
        self.long_time = long_time
        self.short_date = short_date
        self.long_date = long_date
        self.day_of_week = day_of_week
        self.old_text = old_text

    @staticmethod
    def _parse(
        client,
        entity: "raw.base.MessageEntity",
        users: Dict[int, "raw.types.User"] = None,
    ) -> Optional["MessageEntity"]:
        try:
            if isinstance(entity, raw.types.InputMessageEntityMentionName):
                entity_type = enums.MessageEntityType.TEXT_MENTION
                user_id = entity.user_id.user_id
            else:
                entity_type = enums.MessageEntityType(entity.__class__)
                user_id = getattr(entity, "user_id", None)
        except ValueError:
            entity_type = enums.MessageEntityType.UNKNOWN
            user_id = None

        date_val = None
        relative_val = None
        short_time_val = None
        long_time_val = None
        short_date_val = None
        long_date_val = None
        day_of_week_val = None

        if isinstance(entity, raw.types.MessageEntityFormattedDate):
            date_val = entity.date
            relative_val = getattr(entity, "relative", None)
            short_time_val = getattr(entity, "short_time", None)
            long_time_val = getattr(entity, "long_time", None)
            short_date_val = getattr(entity, "short_date", None)
            long_date_val = getattr(entity, "long_date", None)
            day_of_week_val = getattr(entity, "day_of_week", None)

        resolved_user = None
        if users and user_id is not None:
            resolved_user = types.User._parse(client, users.get(user_id, None))

        return MessageEntity(
            type=entity_type,
            offset=entity.offset,
            length=entity.length,
            url=getattr(entity, "url", None),
            user=resolved_user,
            language=getattr(entity, "language", None),
            custom_emoji_id=getattr(entity, "document_id", None),
            collapsed=getattr(entity, "collapsed", None),
            date=date_val,
            relative=relative_val,
            short_time=short_time_val,
            long_time=long_time_val,
            short_date=short_date_val,
            long_date=long_date_val,
            day_of_week=day_of_week_val,
            old_text=getattr(entity, "old_text", None),
            client=client,
        )

    async def write(self):
        args = self.__dict__.copy()

        for arg in ("_client", "type", "user"):
            args.pop(arg)

        if self.user:
            args["user_id"] = await self._client.resolve_peer(self.user.id)

        if not self.url:
            args.pop("url")

        if self.language is None:
            args.pop("language")

        args.pop("custom_emoji_id")
        if self.custom_emoji_id is not None:
            args["document_id"] = self.custom_emoji_id

        if self.type not in (
            enums.MessageEntityType.BLOCKQUOTE,
            enums.MessageEntityType.EXPANDABLE_BLOCKQUOTE,
        ):
            args.pop("collapsed")

        if self.type != enums.MessageEntityType.FORMATTED_DATE:
            for f in ("date", "relative", "short_time", "long_time", "short_date", "long_date", "day_of_week"):
                args.pop(f)

        if self.type != enums.MessageEntityType.DIFF_REPLACE:
            args.pop("old_text")

        entity_cls = self.type.value

        if entity_cls is raw.types.MessageEntityMentionName:
            entity_cls = raw.types.InputMessageEntityMentionName

        return entity_cls(**args)
