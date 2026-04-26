
from typing import Callable, Optional

import pyrogram


class OnStart:
    def on_start(self: Optional["OnStart"] = None) -> Callable:
        """Decorator for handling client start.

        This does the same thing as :meth:`~pyrogram.Client.add_handler` using the
        :obj:`~pyrogram.handlers.StartHandler`.

        .. include:: /_includes/usable-by/users-bots.rst
        """

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyrogram.Client):
                self.add_handler(pyrogram.handlers.StartHandler(func))
            else:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append((pyrogram.handlers.StartHandler(func), 0))

            return func

        return decorator
