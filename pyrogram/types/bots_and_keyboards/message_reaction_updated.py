
from datetime import datetime
from typing import Optional, Dict, List

import pyrogram
from pyrogram import raw, types, utils
from ..object import Object
from ..update import Update


class MessageReactionUpdated(Object, Update):
    """This object represents a change of a reaction on a message performed by a user.
    A reaction to a message was changed by a user.
    The update isn't received for reactions set by bots.

    These updates are heavy and their changes may be delayed by a few minutes.

    Parameters:
        chat (:obj:`~pyrogram.types.Chat`):
            The chat containing the message the user reacted to.

        message_id (``int``):
            Unique identifier of the message inside the chat.

        user (:obj:`~pyrogram.types.User`, *optional*):
            The user that changed the reaction, if the user isn't anonymous.

        actor_chat (:obj:`~pyrogram.types.Chat`, *optional*):
            The chat on behalf of which the reaction was changed, if the user is anonymous.

        date (:py:obj:`~datetime.datetime`):
            Date of change of the reaction.

        old_reaction (List of :obj:`~pyrogram.types.Reaction`):
            Previous list of reaction types that were set by the user.

        new_reaction (List of :obj:`~pyrogram.types.Reaction`):
            New list of reaction types that have been set by the user.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        chat: "types.Chat",
        message_id: int,
        user: "types.User",
        actor_chat: "types.Chat",
        date: datetime,
        old_reaction: List["types.Reaction"],
        new_reaction: List["types.Reaction"]
    ):
        super().__init__(client)

        self.chat = chat
        self.message_id = message_id
        self.user = user
        self.actor_chat = actor_chat
        self.date = date
        self.old_reaction = old_reaction
        self.new_reaction = new_reaction

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        update: "raw.types.UpdateBotMessageReaction",
        users: Dict[int, "raw.types.User"],
        chats: Dict[int, "raw.types.Chat"]
    ) -> "MessageReactionUpdated":
        peer_id = utils.get_peer_id(update.peer)
        raw_peer_id = utils.get_raw_peer_id(update.peer)

        if peer_id > 0:
            chat = types.Chat._parse_user_chat(client, users[raw_peer_id])
        else:
            chat = types.Chat._parse_chat(client, chats[raw_peer_id])

        user = None
        actor_chat = None

        raw_actor_peer_id = utils.get_raw_peer_id(update.actor)
        actor_peer_id = utils.get_peer_id(update.actor)

        if actor_peer_id > 0:
            user = types.User._parse(client, users[raw_actor_peer_id])
        else:
            actor_chat = types.Chat._parse_channel_chat(client, chats[raw_actor_peer_id])

        return MessageReactionUpdated(
            client=client,
            chat=chat,
            message_id=update.msg_id,
            user=user,
            actor_chat=actor_chat,
            date=utils.timestamp_to_datetime(update.date),
            old_reaction=[
                types.Reaction._parse(
                    client,
                    reaction
                ) for reaction in update.old_reactions
            ],
            new_reaction=[
                types.Reaction._parse(
                    client,
                    reaction
                ) for reaction in update.new_reactions
            ]
        )
