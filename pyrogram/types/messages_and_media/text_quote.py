
from typing import Dict, List, Optional

import pyrogram
from pyrogram import raw, types

from ..messages_and_media.message import Str
from ..object import Object

class TextQuote(Object):
    """Describes manually or automatically chosen quote from another message.


    Parameters:
        text (``str``):
            Text of the quoted part of a message that is replied to by the given message.

        entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
            Special entities that appear in the quote.
            Currently, only bold, italic, underline, strikethrough, spoiler, and custom_emoji entities are kept in quotes.

        position (``int``):
            Approximate quote position in the original message in UTF-16 code units as specified by the sender.

        is_manual (``bool``, *optional*):
            True, if the quote was chosen manually by the message sender.
            Otherwise, the quote was added automatically by the server.

    """
    def __init__(
        self, *,
        text: Optional[str] = None,
        entities: Optional[List["types.MessageEntity"]] = None,
        position: Optional[int] = None,
        is_manual: Optional[bool] = None
    ):
        super().__init__()

        self.text = text
        self.entities = entities
        self.position = position
        self.is_manual = is_manual

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        users: Dict[int, "raw.types.User"],
        reply_to: "raw.types.MessageReplyHeader"
    ) -> "TextQuote":
        if isinstance(reply_to, raw.types.MessageReplyHeader):
            entities = types.List(
                filter(
                    lambda x: x is not None,
                    [
                        types.MessageEntity._parse(client, entity, users)
                        for entity in getattr(reply_to, "quote_entities", [])
                    ]
                )
            )

            return TextQuote(
                text=Str(reply_to.quote_text).init(entities) or None,
                entities=entities or None,
                position=reply_to.quote_offset or 0,
                is_manual=reply_to.quote
            )
