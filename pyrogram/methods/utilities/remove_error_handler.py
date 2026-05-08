
from __future__ import annotations
from collections.abc import Iterable
import pyrogram

class RemoveErrorHandler:
    def remove_error_handler(
        self: pyrogram.Client,
        exception: type[Exception] | Iterable[type[Exception]] = Exception,
    ):
        """Remove a previously registered error handler using exception classes.


        Parameters:
            exception (``Exception`` | Iterable of ``Exception``, *optional*):
                The error(s) for handlers to be removed. Defaults to Exception.
        """
        to_remove = [
            handler
            for handler in self.dispatcher.error_handlers
            if handler.check_remove(exception)
        ]
        for handler in to_remove:
            self.dispatcher.error_handlers.remove(handler)
