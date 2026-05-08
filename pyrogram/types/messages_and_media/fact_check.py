from typing import Dict, List, Optional

import pyrogram
from pyrogram import raw, types, utils

from ..object import Object


class FactCheck(Object):
    """Represents a fact-check created by an independent fact-checker.

    Parameters:
        need_check (``bool``, *optional*):
            If set, the country/text fields will not be set, and the fact check must be fetched manually by the client (if it isn't already cached with the key specified in hash) using bundled messages.getFactCheck requests, when the message with the factcheck scrolls into view.

        country (``str``, *optional*):
            A two-letter ISO 3166-1 alpha-2 country code of the country for which the fact-check should be shown.

        text (``str``, *optional*):
            The fact-check.

        entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
            For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text.
    """
    def __init__(
        self, *,
        need_check: Optional[bool] = None,
        country: Optional[str] = None,
        text: Optional[str] = None,
        entities: Optional[List["types.MessageEntity"]] = None
    ):
        super().__init__()

        self.need_check = need_check
        self.country = country
        self.text = text
        self.entities = entities

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        fact_check: "raw.types.FactCheck",
        users: Dict[int, List["raw.base.User"]]
    ) -> Optional["FactCheck"]:
        if not fact_check:
            return None

        message, entities = (utils.parse_text_with_entities(client, getattr(fact_check, "text", None), users)).values()

        return FactCheck(
            need_check=getattr(fact_check, "need_check", None),
            country=getattr(fact_check, "country", None),
            text=message,
            entities=entities
        )
