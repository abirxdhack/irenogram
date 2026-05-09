from typing import Dict, List, Optional

import pyrogram
from pyrogram import raw, types
from ..object import Object


class ChatBoostsList(Object):
    """Represents a list of boosts applied to a chat by a specific user.

    Parameters:
        boosts (List of :obj:`~pyrogram.types.ChatBoost`):
            List of boosts applied to the chat.

        total_count (``int``):
            Total number of boosts applied.

        next_offset (``str``, *optional*):
            Offset for the next page of results, if available.
    """

    def __init__(
        self,
        *,
        boosts: List["types.ChatBoost"],
        total_count: int,
        next_offset: Optional[str] = None,
    ):
        super().__init__()

        self.boosts = boosts
        self.total_count = total_count
        self.next_offset = next_offset

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        boosts_list: "raw.types.premium.BoostsList",
    ) -> "ChatBoostsList":
        users = {u.id: u for u in boosts_list.users}

        return ChatBoostsList(
            boosts=types.List(
                [types.ChatBoost._parse(client, b, users) for b in boosts_list.boosts]
            ),
            total_count=boosts_list.count,
            next_offset=getattr(boosts_list, "next_offset", None),
        )
