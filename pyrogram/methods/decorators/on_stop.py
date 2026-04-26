
from typing import Callable, Optional

import pyrogram


class OnStop:
    def on_stop(self: Optional["OnStop"] = None) -> Callable:
        """Decorator for handling client stop.

        This does the same thing as :meth:`~pyrogram.Client.add_handler` using the
        :obj:`~pyrogram.handlers.StopHandler`.

        .. include:: /_includes/usable-by/users-bots.rst
        """

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyrogram.Client):
                self.add_handler(pyrogram.handlers.StopHandler(func))
            else:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append((pyrogram.handlers.StopHandler(func), 0))

            return func

        return decorator
