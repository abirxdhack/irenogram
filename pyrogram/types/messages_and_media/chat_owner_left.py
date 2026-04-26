
from typing import Dict, Optional

import pyrogram
from pyrogram import raw, types

from ..object import Object


class ChatOwnerLeft(Object):
    """Describes a service message about the chat owner leaving the chat.

    Parameters:
        new_owner (:obj:`~pyrogram.types.User`, *optional*):
            The user which will be the new owner of the chat if the previous owner does not return to the chat.
    """

    def __init__(self, *, new_owner: Optional["types.User"] = None):
        super().__init__()

        self.new_owner = new_owner

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        action: "raw.types.MessageActionNewCreatorPending",
        users: Dict[int, "types.User"],
    ) -> "ChatOwnerLeft":
        if isinstance(action, raw.types.MessageActionNewCreatorPending):
            return ChatOwnerLeft(
                new_owner=types.User._parse(client, users.get(action.new_creator_id))
            )
