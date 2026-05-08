
from typing import Callable, Optional

import pyrogram


class OnConnect:
    def on_connect(self: Optional["OnConnect"] = None) -> Callable:
        """Decorator for handling connections.

        This does the same thing as :meth:`~pyrogram.Client.add_handler` using the
        :obj:`~pyrogram.handlers.ConnectHandler`.

        .. include:: /_includes/usable-by/users-bots.rst
        """

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyrogram.Client):
                self.add_handler(pyrogram.handlers.ConnectHandler(func))
            else:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append((pyrogram.handlers.ConnectHandler(func), 0))

            return func

        return decorator
