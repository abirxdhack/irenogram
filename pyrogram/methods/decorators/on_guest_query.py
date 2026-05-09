from typing import Callable

import pyrogram
from pyrogram.filters import Filter


class OnGuestQuery:
    def on_guest_query(
        self=None,
        filters=None,
        group: int = 0,
    ) -> Callable:
        """Decorator for handling incoming guest chat queries.

        This does the same thing as :meth:`~pyrogram.Client.add_handler` using the
        :obj:`~pyrogram.handlers.GuestQueryHandler`.

        Parameters:
            filters (:obj:`~pyrogram.filters`, *optional*):
                Pass one or more filters to allow only a subset of guest queries to be passed
                in your function.

            group (``int``, *optional*):
                The group identifier, defaults to 0.
        """

        def decorator(func: Callable) -> Callable:
            """Return a decorator that registers the decorated function as a handler."""
            if isinstance(self, pyrogram.Client):
                self.add_handler(pyrogram.handlers.GuestQueryHandler(func, filters), group)
            elif isinstance(self, Filter) or self is None:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append(
                    (
                        pyrogram.handlers.GuestQueryHandler(func, self),
                        group if filters is None else filters,
                    )
                )

            return func

        return decorator
