import asyncio
import base64
import datetime
import logging
from typing import List, Optional

import pyrogram
from pyrogram import raw, types

log = logging.getLogger(__name__)


class QRLogin:
    """Handles the QR code login flow for Irenogram."""

    def __init__(self, client: "pyrogram.Client", except_ids: List[int] = None):
        self.client = client
        self.except_ids = except_ids or []
        self.r: "raw.base.auth.LoginToken" = None

    async def recreate(self):
        """Request a fresh QR code token from Telegram and store the raw response."""
        self.r = await self.client.invoke(
            raw.functions.auth.ExportLoginToken(
                api_id=self.client.api_id,
                api_hash=self.client.api_hash,
                except_ids=self.except_ids,
            )
        )

    @property
    def url(self) -> str:
        """The tg:// deep-link URL that encodes the current login token."""
        return "tg://login?token={}".format(
            base64.urlsafe_b64encode(self.r.token).decode("utf-8")
        )

    async def wait(self, timeout: float = None) -> Optional["types.User"]:
        """Wait until the QR code is scanned and return the logged-in :obj:`~pyrogram.types.User`.

        Parameters:
            timeout (``float``, *optional*):
                Maximum seconds to wait before raising :exc:`asyncio.TimeoutError`.
                Defaults to the token's own expiry window.

        Returns:
            :obj:`~pyrogram.types.User`: The authorised user.

        Raises:
            asyncio.TimeoutError: The token expired before being scanned.
            ~pyrogram.errors.SessionPasswordNeeded: The account has 2FA enabled.
            ~pyrogram.errors.AuthTokenExpired: The auth token has expired.
        """
        if timeout is None:
            timeout = self.r.expires - int(datetime.datetime.now().timestamp())

        async def _poll() -> Optional["types.User"]:
            while True:
                r = await self.client.invoke(
                    raw.functions.auth.ExportLoginToken(
                        api_id=self.client.api_id,
                        api_hash=self.client.api_hash,
                        except_ids=self.except_ids,
                    )
                )

                if isinstance(r, raw.types.auth.LoginTokenMigrateTo):
                    await self.client.set_dc(r.dc_id)
                    r = await self.client.invoke(
                        raw.functions.auth.ImportLoginToken(token=r.token)
                    )

                if isinstance(r, raw.types.auth.LoginTokenSuccess):
                    user = types.User._parse(self.client, r.authorization.user)
                    await self.client.storage.user_id(user.id)
                    await self.client.storage.is_bot(False)
                    return user

                await asyncio.sleep(3)

        return await asyncio.wait_for(_poll(), timeout=timeout)
