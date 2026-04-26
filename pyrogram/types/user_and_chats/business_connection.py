
from datetime import datetime
from typing import Optional, Union

from pyrogram import types, raw, utils
from ..object import Object


class BusinessConnection(Object):
    """Business information of a user.

    Parameters:
        id (``str``):
            Unique identifier of the business connection that belongs to the user.

        user (:obj:`~pyrogram.types.User`):
            Business account user that created the business connection.

        dc_id (``int``):
            Datacenter identifier of the user.

        date (:py:obj:`~datetime.datetime`):
            Date the connection was established in Unix time.

        is_enabled (``bool``, *optional*):
            True, if the connection is active.

        permissions (:obj:`~pyrogram.types.BusinessBotPermissions`, *optional*):
            Permissions for the business bot.
    """

    def __init__(
        self,
        *,
        id: str,
        user: "types.User",
        dc_id: int,
        date: datetime,
        is_enabled: bool = None,
        rights: "types.BusinessBotRights" = None
    ):
        self.id = id
        self.user = user
        self.dc_id = dc_id
        self.date = date
        self.is_enabled = is_enabled
        self.rights = rights

    @staticmethod
    def _parse(
        client,
        connection: Union["raw.types.BotBusinessConnection", "raw.types.UpdateBotBusinessConnect"] = None,
        users = {}
    ) -> Optional["BusinessConnection"]:
        if not connection:
            return None

        if isinstance(connection, raw.types.UpdateBotBusinessConnect):
            connection = connection.connection

        return BusinessConnection(
            id=connection.connection_id,
            user=types.User._parse(client, users.get(connection.user_id)),
            dc_id=connection.dc_id,
            date=utils.timestamp_to_datetime(connection.date),
            is_enabled=not connection.disabled,
            rights=types.BusinessBotRights._parse(connection.rights)
        )
