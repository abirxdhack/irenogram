
from time import time

import pyrogram
from pyrogram import raw

class Ping:
    async def ping(self: "pyrogram.Client"):
        """Measure the round-trip time (RTT) to the Telegram server.

        The ping method sends a request to the Telegram server and measures the time it takes to receive a response.
        This can be useful for monitoring network latency and ensuring a stable connection to the server.

        Returns:
            float: The round-trip time in milliseconds (ms).

        Example:
            .. code-block:: python

                latency = await app.ping()
                print(f"Ping: {latency} ms")
        """
        start_time = time()
        await self.invoke(
            raw.functions.ping.Ping(ping_id=self.rnd_id()),
        )
        return round((time() - start_time) * 1000.0, 3)
