from pyrogram import raw
from .auto_name import AutoName


class MessageEntityType(AutoName):
    """Message entity type enumeration used in :obj:`~pyrogram.types.MessageEntity`."""

    MENTION = raw.types.MessageEntityMention
    "``@username``"

    HASHTAG = raw.types.MessageEntityHashtag
    "``#hashtag``"

    CASHTAG = raw.types.MessageEntityCashtag
    "``$USD``"

    BOT_COMMAND = raw.types.MessageEntityBotCommand
    "``/start@pyrogrambot``"

    URL = raw.types.MessageEntityUrl
    "``https://pyrogram.org`` (see ``url``)"

    EMAIL = raw.types.MessageEntityEmail
    "``do-not-reply@pyrogram.org``"

    PHONE_NUMBER = raw.types.MessageEntityPhone
    "``+1-123-456-7890``"

    BOLD = raw.types.MessageEntityBold
    "Bold text"

    ITALIC = raw.types.MessageEntityItalic
    "Italic text"

    UNDERLINE = raw.types.MessageEntityUnderline
    "Underlined text"

    STRIKETHROUGH = raw.types.MessageEntityStrike
    "Strikethrough text"

    SPOILER = raw.types.MessageEntitySpoiler
    "Spoiler text"

    CODE = raw.types.MessageEntityCode
    "Monowidth string"

    PRE = raw.types.MessageEntityPre
    "Monowidth block (see ``language``)"

    BLOCKQUOTE = raw.types.MessageEntityBlockquote
    "Blockquote text"

    EXPANDABLE_BLOCKQUOTE = raw.types.MessageEntityBlockquote
    "Collapsed-by-default block quotation"

    TEXT_LINK = raw.types.MessageEntityTextUrl
    "For clickable text URLs"

    TEXT_MENTION = raw.types.MessageEntityMentionName
    "For users without usernames (see ``user``)"

    BANK_CARD = raw.types.MessageEntityBankCard
    "Bank card text"

    CUSTOM_EMOJI = raw.types.MessageEntityCustomEmoji
    "Custom emoji"

    FORMATTED_DATE = raw.types.MessageEntityFormattedDate
    "Date/time entity with formatting flags (relative, short_time, long_time, short_date, long_date, day_of_week)"

    DIFF_INSERT = raw.types.MessageEntityDiffInsert
    "Inserted text in a diff view"

    DIFF_REPLACE = raw.types.MessageEntityDiffReplace
    "Replaced text in a diff view (see ``old_text``)"

    DIFF_DELETE = raw.types.MessageEntityDiffDelete
    "Deleted text in a diff view"

    UNKNOWN = raw.types.MessageEntityUnknown
    "Unknown message entity type"
