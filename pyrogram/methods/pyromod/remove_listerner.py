
import pyrogram
from pyrogram.types import Listener

class RemoveListener:
    def remove_listener(
        self: "pyrogram.Client",
        listener: Listener
    ):
        """Removes a listener from the :meth:`~pyrogram.Client.listeners` dictionary.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            listener (:obj:`~pyrogram.types.Listener`):
                The listener to remove.
        """
        try:
            self.listeners[listener.listener_type].remove(listener)
        except ValueError:
            pass
