
import asyncio
import inspect
import pyrogram

from pyrogram.errors import ListenerTimeout
from pyrogram.filters import Filter
from typing import List, Optional, Union
from pyrogram.types import Identifier, Listener
from pyrogram.utils import PyromodConfig

class Listen:
    async def listen(
        self: "pyrogram.Client",
        filters: Optional[Filter] = None,
        listener_type: "pyrogram.enums.ListenerTypes" = pyrogram.enums.ListenerTypes.MESSAGE,
        timeout: Optional[int] = None,
        unallowed_click_alert: bool = True,
        chat_id: Union[Union[int, str], List[Union[int, str]]] = None,
        user_id: Union[Union[int, str], List[Union[int, str]]] = None,
        message_id: Union[int, List[int]] = None,
        inline_message_id: Union[str, List[str]] = None,
    ):
        """Listen for a message, callback query, etc.

        Message:

        .. include:: /_includes/usable-by/users-bots.rst

        CallbackQuery:

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            chat_id (``int`` | ``str`` | Iterable of ``int`` | Iterable of ``str``, *optional*):
                Unique identifier (int) or username (str) of the target chat.

            user_id (``int`` | ``str`` | Iterable of ``int`` | Iterable of ``str``, *optional*):
                The user ID to listen for.

            filters (:obj:`~pyrogram.filters`, *optional*):
                A filter to check the incoming message against.

            listener_type (:obj:`~pyrogram.enums.ListenerTypes`, *optional*):
                The type of listener to listen for.
                Default to Message.

            timeout (``int``, *optional*):
                The maximum amount of time to wait for a message.

            unallowed_click_alert (``bool``, *optional*):
                Whether to alert the user if they click a button that doesn’t match the filters.
                Default to True.

            message_id (``int``, *optional*):
                The message ID to listen for.

            inline_message_id (``str``, *optional*):
                The inline message ID to listen for.

        Returns:
            :obj:`~pyrogram.types.Message` | :obj:`~pyrogram.types.CallbackQuery`: On success, a message/callbackquery is returned.

        Example:
            .. code-block:: python

                await app.listen(chat_id)
        """

        pattern = Identifier(
            from_user_id=user_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
        )

        loop = asyncio.get_running_loop()
        future = loop.create_future()

        listener = Listener(
            future=future,
            filters=filters,
            unallowed_click_alert=unallowed_click_alert,
            identifier=pattern,
            listener_type=listener_type,
        )

        future.add_done_callback(lambda _future: self.remove_listener(listener))

        self.listeners[listener_type].append(listener)

        try:
            return await asyncio.wait_for(future, timeout)
        except asyncio.exceptions.TimeoutError:
            if callable(PyromodConfig.timeout_handler):
                if inspect.iscoroutinefunction(PyromodConfig.timeout_handler.__call__):
                    await PyromodConfig.timeout_handler(pattern, listener, timeout)
                else:
                    await asyncio.get_event_loop().run_in_executor(
                        None, PyromodConfig.timeout_handler, pattern, listener, timeout
                    )
            elif PyromodConfig.throw_exceptions:
                raise ListenerTimeout(timeout)
