import asyncio
import base64
from typing import Optional, List

import pyrogram
from pyrogram import raw, types


class QRLogin:
    """QR Code Login handler for Pyrogram."""

    def __init__(self, client: "pyrogram.Client", except_ids: List[int] = None):
        self.client = client
        self.except_ids = except_ids or []
        self.token: Optional[bytes] = None
        self.url: Optional[str] = None
        self.expires_in: Optional[int] = None

    async def request(self) -> "QRLogin":
        """Request a new QR code token."""
        r = await self.client.invoke(
            raw.functions.auth.ExportLoginToken(
                api_id=self.client.api_id,
                api_hash=self.client.api_hash,
                except_ids=self.except_ids
            )
        )

        if isinstance(r, raw.types.auth.LoginToken):
            self.token = r.token
            self.url = f"tg://login?token={base64.urlsafe_b64encode(r.token).decode().rstrip('=')}"
            self.expires_in = r.expires - int(asyncio.get_event_loop().time())

        return self

    async def wait(self, timeout: float = 30) -> Optional["types.User"]:
        """Wait for the QR code to be scanned."""
        try:
            updates = await asyncio.wait_for(
                self._poll(),
                timeout=timeout
            )
            return updates
        except asyncio.TimeoutError:
            return None

    async def _poll(self) -> Optional["types.User"]:
        while True:
            try:
                r = await self.client.invoke(
                    raw.functions.auth.ExportLoginToken(
                        api_id=self.client.api_id,
                        api_hash=self.client.api_hash,
                        except_ids=self.except_ids
                    )
                )

                if isinstance(r, raw.types.auth.LoginTokenSuccess):
                    auth = r.authorization
                    if isinstance(auth, raw.types.auth.Authorization):
                        await self.client.storage.user_id(auth.user.id)
                        await self.client.storage.is_bot(False)
                        return types.User._parse(self.client, auth.user)

                if isinstance(r, raw.types.auth.LoginTokenMigrateTo):
                    await self.client._switch_dc(r.dc_id)
                    continue

            except Exception:
                pass

            await asyncio.sleep(1)
