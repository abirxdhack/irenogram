from typing import Dict

import pyrogram
from pyrogram import raw, types, utils

from ..object import Object


class ProximityAlertTriggered(Object):
    """Information about a proximity alert.

    Parameters:
        traveler (:obj:`~pyrogram.types.User`):
            Chat that triggered the proximity alert.

        watcher (:obj:`~pyrogram.types.User`):
            Chat that subscribed for the proximity alert.

        distance (``str``):
            The distance between the users.
    """
    def __init__(
        self, *,
        traveler: "pyrogram.types.User",
        watcher: "pyrogram.types.User",
        distance: str
    ):
        super().__init__()

        self.traveler = traveler
        self.watcher = watcher
        self.distance = distance

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        action: "raw.types.MessageActionGeoProximityReached",
        users: Dict[int, "raw.base.User"],
        chats: Dict[int, "raw.base.Chat"]
    ) -> "ProximityAlertTriggered":
        from_id = utils.get_raw_peer_id(action.from_id)
        to_id = utils.get_raw_peer_id(action.to_id)

        return ProximityAlertTriggered(
            traveler=types.Chat._parse_chat(client, users.get(from_id) or chats.get(from_id)),
            watcher=types.Chat._parse_chat(client, users.get(to_id) or chats.get(to_id)),
            distance=action.distance
        )
