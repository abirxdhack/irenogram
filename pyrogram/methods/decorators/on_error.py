
from typing import Callable

import pyrogram
from pyrogram.filters import Filter

class OnError:
    def on_error(
        self=None,
        errors=None,
        group: int = 0,
    ) -> Callable:
        """Decorator for handling new errors.

        This does the same thing as :meth:`~pyrogram.Client.add_handler` using the
        :obj:`~pyrogram.handlers.ErrorHandler`.

        Parameters:
            errors (:obj:`~Exception`, *optional*):
                Pass one or more errors to allow only a subset of errors to be passed
                in your function.

            group (``int``, *optional*):
                The group identifier, defaults to 0.
        """

        def decorator(func: Callable) -> Callable:
            """Return a decorator that registers the decorated function as a handler."""
            if isinstance(self, pyrogram.Client):
                self.add_handler(pyrogram.handlers.ErrorHandler(func, errors), group)
            elif isinstance(self, Filter) or self is None:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append((pyrogram.handlers.ErrorHandler(func, self), group))

            return func

        return decorator
