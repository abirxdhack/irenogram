
from typing import Optional, List, Dict

import pyrogram
from pyrogram import raw, types
from ..object import Object

class MessageReactions(Object):
    """Contains information about a message reactions.


    Parameters:
        reactions (List of :obj:`~pyrogram.types.Reaction`):
            Reactions list.

        top_reactors (List of :obj:`~pyrogram.types.MessageReactor`):
            Top reactors.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        reactions: Optional[List["types.Reaction"]] = None,
        top_reactors: Optional[List["types.MessageReactor"]] = None
    ):
        super().__init__(client)

        self.reactions = reactions
        self.top_reactors = top_reactors

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        message_reactions: Optional["raw.base.MessageReactions"] = None,
        users: Optional[Dict[int, "raw.types.User"]] = None,
        chats: Dict[int, "raw.types.Chat"] = None
    ) -> Optional["MessageReactions"]:
        if not message_reactions:
            return None

        return MessageReactions(
            client=client,
            reactions=[
                types.Reaction._parse_count(client, reaction)
                for reaction in message_reactions.results
            ],
            top_reactors=[
                types.MessageReactor._parse(client, reactor, users, chats)
                for reactor in message_reactions.top_reactors
            ]
        )
