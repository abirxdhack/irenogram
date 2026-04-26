
from datetime import datetime
from typing import Dict, Optional

import pyrogram
from pyrogram import enums, raw, types, utils

from ..object import Object

class MessageOrigin(Object):
    """This object describes the origin of a message.

    It can be one of:

    - :obj:`~pyrogram.types.MessageOriginChannel`
    - :obj:`~pyrogram.types.MessageOriginChat`
    - :obj:`~pyrogram.types.MessageOriginHiddenUser`
    - :obj:`~pyrogram.types.MessageOriginImport`
    - :obj:`~pyrogram.types.MessageOriginUser`
    """

    def __init__(
        self,
        type: "enums.MessageOriginType",
        date: Optional[datetime] = None
    ):
        super().__init__()

        self.type = type
        self.date = date

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        fwd_from: "raw.types.MessageFwdHeader",
        users: Dict[int, "raw.base.User"],
        chats: Dict[int, "raw.base.Chat"]
    ) -> Optional["MessageOrigin"]:
        if not fwd_from:
            return None

        forward_date = utils.timestamp_to_datetime(fwd_from.date)

        if fwd_from.from_id:
            raw_peer_id = utils.get_raw_peer_id(fwd_from.from_id)
            peer_id = utils.get_peer_id(fwd_from.from_id)
            peer_type = utils.get_peer_type(peer_id)

            if peer_type == "user":
                return types.MessageOriginUser(
                    date=forward_date,
                    sender_user=types.User._parse(client, users.get(raw_peer_id))
                )
            else:
                if fwd_from.channel_post:
                    return types.MessageOriginChannel(
                        date=forward_date,
                        chat=types.Chat._parse_channel_chat(client, chats.get(raw_peer_id)),
                        message_id=fwd_from.channel_post,
                        author_signature=fwd_from.post_author
                    )
                else:
                    return types.MessageOriginChat(
                        date=forward_date,
                        sender_chat=types.Chat._parse_channel_chat(client, chats.get(raw_peer_id)),
                        author_signature=fwd_from.post_author
                    )
        elif fwd_from.from_name:
            return types.MessageOriginHiddenUser(
                date=forward_date,
                sender_user_name=fwd_from.from_name
            )
        elif fwd_from.imported:
            return types.MessageOriginImport(
                date=forward_date,
                sender_user_name=fwd_from.post_author
            )
