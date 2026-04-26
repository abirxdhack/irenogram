
import pyrogram

from typing import List
from pyrogram.types import Identifier, Listener

class GetManyListenersMatchingWithData:
    def get_many_listeners_matching_with_data(
        self: "pyrogram.Client",
        data: Identifier,
        listener_type: "pyrogram.enums.ListenerTypes",
    ) -> List[Listener]:
        """Gets multiple listener that matches the given data.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            data (:obj:`~pyrogram.types.Identifier`):
                The Identifier to match agains.

            listener_type (:obj:`~pyrogram.enums.ListenerTypes`):
                The type of listener to get.

        Returns:
            List of :obj:`~pyrogram.types.Listener`: On success, a list of Listener is returned.
        """
        listeners = []
        for listener in self.listeners[listener_type]:
            if listener.identifier.matches(data):
                listeners.append(listener)
        return listeners
