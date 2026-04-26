
import inspect
import pyrogram

from pyrogram.errors import ListenerStopped
from pyrogram.types import Listener
from pyrogram.utils import PyromodConfig

class StopListener:
    async def stop_listener(
        self: "pyrogram.Client",
        listener: Listener
    ):
        """Stops a listener, calling stopped_handler if applicable or raising ListenerStopped if throw_exceptions is True.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            listener (:obj:`~pyrogram.types.Listener`):
                The listener to remove.

        Raises:
            :raises ~pyrogram.errors.ListenerStopped: If throw_exceptions is True.
        """
        self.remove_listener(listener)

        if listener.future.done():
            return

        if callable(PyromodConfig.stopped_handler):
            if inspect.iscoroutinefunction(PyromodConfig.stopped_handler.__call__):
                await PyromodConfig.stopped_handler(None, listener)
            else:
                await asyncio.get_event_loop().run_in_executor(
                    None, PyromodConfig.stopped_handler, None, listener
                )
        elif PyromodConfig.throw_exceptions:
            listener.future.set_exception(ListenerStopped())
