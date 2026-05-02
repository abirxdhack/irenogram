import logging
from typing import List

import pyrogram
from pyrogram import raw

log = logging.getLogger(__name__)


class Start:
    async def start(
        self: "pyrogram.Client",
        *,
        use_qr: bool = False,
        except_ids: List[int] = [],
    ):
        """Start the client.

        This method connects the client to Telegram and, in case of new sessions, automatically manages the
        authorization process using an interactive prompt or a QR code.

        .. note::

            Install the ``qrcode`` package to use QR code authorization:
            ``pip install qrcode``

        Parameters:
            use_qr (``bool``, *optional*):
                Use QR code authorization instead of the interactive phone-number prompt.
                Only applies to new (unauthorized) sessions.
                Defaults to False.

            except_ids (List of ``int``, *optional*):
                List of already logged-in user IDs to exclude during QR authorization,
                preventing the same account from being logged in twice.
                Only used when *use_qr* is True.

        Returns:
            :obj:`~pyrogram.Client`: The started client itself.

        Raises:
            ConnectionError: In case you try to start an already started client.

        Example:
            .. code-block:: python

                import asyncio
                from pyrogram import Client

                async def main():
                    app = Client("my_account")
                    await app.start()
                    ...
                    await app.stop()

                asyncio.run(main())

        Example with QR code:
            .. code-block:: python

                import asyncio
                from pyrogram import Client

                async def main():
                    app = Client("my_account", api_id=12345, api_hash="...")
                    await app.start(use_qr=True)
                    print(await app.get_me())
                    await app.stop()

                asyncio.run(main())
        """
        self.load_plugins()

        is_authorized = await self.connect()

        try:
            if not is_authorized:
                if use_qr:
                    try:
                        import qrcode
                        await self.authorize_qr(except_ids=except_ids)
                    except ImportError:
                        log.warning("qrcode package not found, falling back to phone number authorization")
                        await self.authorize()
                else:
                    await self.authorize()

            if not await self.storage.is_bot() and self.takeout:
                self.takeout_id = (await self.invoke(raw.functions.account.InitTakeoutSession())).id
                log.info("Takeout session %s initiated", self.takeout_id)

            await self.invoke(raw.functions.updates.GetState())
        except (Exception, KeyboardInterrupt):
            await self.disconnect()
            raise
        else:
            self.me = await self.get_me()
            await self.initialize()

            return self
