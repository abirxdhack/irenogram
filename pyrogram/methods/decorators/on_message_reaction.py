
from typing import Callable

import pyrogram
from pyrogram.filters import Filter


class OnMessageReaction:
    def on_message_reaction(
        self=None,
        filters=None,
        group: int = 0
    ) -> Callable:
        """Decorator for handling reaction changes on messages.

        This does the same thing as :meth:`~pyrogram.Client.add_handler` using the
        :obj:`~pyrogram.handlers.MessageReactionHandler`.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            filters (:obj:`~pyrogram.filters`, *optional*):
                Pass one or more filters to allow only a subset of updates to be passed in your function.

            group (``int``, *optional*):
                The group identifier, defaults to 0.
        """

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyrogram.Client):
                self.add_handler(pyrogram.handlers.MessageReactionHandler(func, filters), group)
            elif isinstance(self, Filter) or self is None:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append(
                    (
                        pyrogram.handlers.MessageReactionHandler(func, self),
                        group if filters is None else filters
                    )
                )

            return func

        return decorator
