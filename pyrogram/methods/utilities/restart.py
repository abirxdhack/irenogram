
import asyncio
import pyrogram

class Restart:
    async def restart(
        self: "pyrogram.Client",
        block: bool = True
    ):
        """Restart the Client.

        This method will first call :meth:`~pyrogram.Client.stop` and then :meth:`~pyrogram.Client.start` in a row in
        order to restart a client using a single method.

        Parameters:
            block (``bool``, *optional*):
                Blocks the code execution until the client has been restarted. It is useful with ``block=False`` in case
                you want to restart the own client within an handler in order not to cause a deadlock.
                Defaults to True.

        Returns:
            :obj:`~pyrogram.Client`: The restarted client itself.

        Raises:
            :raises ConnectionError: In case you try to restart a stopped Client.

        Example:
            .. code-block:: python

                from pyrogram import Client

                app = Client("my_account")

                async def main():
                    await app.start()
                    ...
                    await app.restart()
                    ...
                    await app.stop()

                app.run(main())
        """

        async def do_it():
            """Perform the restart or stop action on the client."""
            await self.stop()
            await self.start()

        if block:
            await do_it()
        else:
            asyncio.get_event_loop().create_task(do_it())

        return self
