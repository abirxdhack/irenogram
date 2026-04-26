
import pyrogram

from typing import Optional
from pyrogram.types import Identifier, Listener

class GetListenerMatchingWithData:
    def get_listener_matching_with_data(
        self: "pyrogram.Client",
        data: Identifier,
        listener_type: "pyrogram.enums.ListenerTypes"
    ) -> Optional[Listener]:
        """Gets a listener that matches the given data.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            data (:obj:`~pyrogram.types.Identifier`):
                The Identifier to match agains.

            listener_type (:obj:`~pyrogram.enums.ListenerTypes`):
                The type of listener to get.

        Returns:
            :obj:`~pyrogram.types.Listener`: On success, a Listener is returned.
        """
        matching = []
        for listener in self.listeners[listener_type]:
            if listener.identifier.matches(data):
                matching.append(listener)

        def count_populated_attributes(listener_item: Listener):
            """Count the number of non-None attributes on this listener identifier."""
            return listener_item.identifier.count_populated()

        return max(matching, key=count_populated_attributes, default=None)
