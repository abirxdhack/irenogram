
import asyncio
import inspect

import pyrogram
from pyrogram.methods.utilities.idle import idle

class Run:
    def run(
        self: "pyrogram.Client",
        coroutine=None
    ):
        """Start the client, idle the main script and finally stop the client.

        When called without an argument, acts as a convenience method that calls
        :meth:`~pyrogram.Client.start`, :meth:`~pyrogram.idle` and
        :meth:`~pyrogram.Client.stop` in sequence.

        If a coroutine is passed, runs it until complete without managing the
        client lifecycle. Equivalent to ``asyncio.run()`` but reuses the current
        event loop.

        Parameters:
            coroutine (``Coroutine``, *optional*):
                Pass a coroutine to run it until it completes.

        Raises:
            :raises ConnectionError: In case you try to run an already started client.

        Example:
            .. code-block:: python

                from pyrogram import Client

                app = Client("my_account")
                app.run()

            .. code-block:: python

                from pyrogram import Client

                app = Client("my_account")

                async def main():
                    async with app:
                        print(await app.get_me())

                app.run(main())
        """
        try:
            loop = asyncio.get_event_loop()
            if loop.is_closed():
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        run = loop.run_until_complete

        if coroutine is not None:
            run(coroutine)
        else:
            if inspect.iscoroutinefunction(self.start):
                run(self.start())
                run(idle())
                run(self.stop())
            else:
                self.start()
                run(idle())
                self.stop()
