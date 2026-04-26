
import pyrogram

from typing import List
from pyrogram.types import Identifier, Listener

class GetManyListenersMatchingWithIdentifierPattern:
    def get_many_listeners_matching_with_identifier_pattern(
        self: "pyrogram.Client",
        pattern: Identifier,
        listener_type: "pyrogram.enums.ListenerTypes",
    ) -> List[Listener]:
        """Gets multiple listener that matches the given identifier pattern.

        .. include:: /_includes/usable-by/users-bots.rst

        The difference from :meth:`~pyrogram.Client.get_listener_matching_with_data` is that this method
        intends to get a listener by passing partial info of the listener identifier, while the other method
        intends to get a listener by passing the full info of the update data, which the listener should match with.

        Parameters:
            pattern (:obj:`~pyrogram.types.Identifier`):
                The Identifier to match agains.

            listener_type (:obj:`~pyrogram.enums.ListenerTypes`):
                The type of listener to get.

        Returns:
            List of :obj:`~pyrogram.types.Listener`: On success, a list of Listener is returned.
        """
        listeners = []
        for listener in self.listeners[listener_type]:
            if pattern.matches(listener.identifier):
                listeners.append(listener)
        return listeners
