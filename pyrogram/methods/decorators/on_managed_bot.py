
from typing import Callable

import pyrogram
from pyrogram.filters import Filter

class OnManagedBot:
    def on_managed_bot(
        self=None,
        filters=None,
        group: int = 0
    ) -> Callable:
        """Decorator for handling managed bot updates.

        This does the same thing as :meth:`~pyrogram.Client.add_handler` using the
        :obj:`~pyrogram.handlers.ManagedBotHandler`.

        Parameters:
            filters (:obj:`~pyrogram.filters`, *optional*):
                Pass one or more filters to allow only a subset of managed bot updates to be passed
                in your function.

            group (``int``, *optional*):
                The group identifier, defaults to 0.
        """

        def decorator(func: Callable) -> Callable:
            """Return a decorator that registers the decorated function as a handler."""
            if isinstance(self, pyrogram.Client):
                self.add_handler(pyrogram.handlers.ManagedBotHandler(func, filters), group)
            elif isinstance(self, Filter) or self is None:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append(
                    (
                        pyrogram.handlers.ManagedBotHandler(func, self),
                        group if filters is None else filters
                    )
                )

            return func

        return decorator
