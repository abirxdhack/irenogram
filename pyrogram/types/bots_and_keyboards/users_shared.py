
from typing import Dict, List, Optional, Union

import pyrogram
from pyrogram import raw, types, utils

from ..object import Object


class UsersShared(Object):
    """Contains information about a users shared with a bot.

    Parameters:
        button_id (``int``):
            Identifier of button.

        users (List of :obj:`~pyrogram.types.User`):
            List of requested users.
    """
    def __init__(
        self, *,
        button_id: int,
        users: List["types.User"],
    ):
        super().__init__()

        self.button_id = button_id
        self.users = users

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        action: Union[
            "raw.types.MessageActionRequestedPeer",
            "raw.types.MessageActionRequestedPeerSentMe"
        ],
        users: Dict[int, "raw.base.User"] = {}
    ) -> Optional["UsersShared"]:
        requested_users = types.List()

        for peer in action.peers:
            peer_id = utils.get_peer_id(peer)

            if isinstance(action, raw.types.MessageActionRequestedPeer):
                raw_user = users.get(utils.get_raw_peer_id(peer))

                if raw_user:
                    requested_users.append(types.User._parse(client, raw_user))
                else:
                    requested_users.append(types.User(id=peer_id, client=client))
            elif isinstance(action, raw.types.MessageActionRequestedPeerSentMe):
                requested_users.append(
                    types.User(
                        id=peer_id,
                        first_name=getattr(peer, "first_name", None),
                        last_name=getattr(peer, "last_name", None),
                        username=getattr(peer, "username", None),
                        photo=types.Photo._parse(client, getattr(peer, "photo", None)),
                        client=client
                    )
                )

        return UsersShared(
            button_id=action.button_id,
            users=requested_users
        )
