
from datetime import datetime
from typing import Optional

import pyrogram
from pyrogram import raw, utils
from ..object import Object

class Passkey(Object):
    """A passkey registered for Telegram authentication.


    Parameters:
        id (``str``): Unique passkey identifier (credential ID).
        name (``str``): Human-readable name for the passkey.
        date (:py:obj:`~datetime.datetime`): When the passkey was registered.
        software_emoji_id (``int``, *optional*): Custom emoji ID representing the passkey software.
        last_usage_date (:py:obj:`~datetime.datetime`, *optional*): When the passkey was last used.
    """

    def __init__(self, *, client=None, id: str, name: str, date: datetime,
                 software_emoji_id: int = None, last_usage_date: datetime = None):
        super().__init__(client)
        self.id = id
        self.name = name
        self.date = date
        self.software_emoji_id = software_emoji_id
        self.last_usage_date = last_usage_date

    @staticmethod
    def _parse(client, p: "raw.types.Passkey") -> "Passkey":
        return Passkey(
            client=client,
            id=p.id,
            name=p.name,
            date=utils.timestamp_to_datetime(p.date),
            software_emoji_id=getattr(p, "software_emoji_id", None),
            last_usage_date=utils.timestamp_to_datetime(getattr(p, "last_usage_date", None)),
        )

    async def delete(self) -> bool:
        """Delete this passkey.

        Returns:
            ``bool``: True on success.
        """
        return await self._client.invoke(
            raw.functions.account.DeletePasskey(id=self.id)
        )
