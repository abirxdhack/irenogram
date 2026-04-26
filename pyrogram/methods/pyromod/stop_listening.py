
import pyrogram

from typing import List, Union
from pyrogram.types import Identifier

class StopListening:
    async def stop_listening(
        self: "pyrogram.Client",
        listener_type: "pyrogram.enums.ListenerTypes" = pyrogram.enums.ListenerTypes.MESSAGE,
        chat_id: Union[Union[int, str], List[Union[int, str]]] = None,
        user_id: Union[Union[int, str], List[Union[int, str]]] = None,
        message_id: Union[int, List[int]] = None,
        inline_message_id: Union[str, List[str]] = None,
    ):
        """Stops all listeners that match the given identifier pattern.

        .. include:: /_includes/usable-by/users-bots.rst

        Uses :meth:`~pyrogram.Client.get_many_listeners_matching_with_identifier_pattern`.

        Parameters:
            listener_type (:obj:`~pyrogram.enums.ListenerTypes`, *optional*):
                The type of listener to stop listening for.
                Default to Message.

            chat_id (``int`` | ``str`` | Iterable of ``int`` | Iterable of ``str``, *optional*):
                Unique identifier (int) or username (str) of the target chat.

            user_id (``int`` | ``str`` | Iterable of ``int`` | Iterable of ``str``, *optional*):
                The user ID to stop listening for.

            message_id (``int``, *optional*):
                The message ID to stop listening for.

            inline_message_id (``str``, *optional*):
                The inline message ID to stop listening for.
        """
        pattern = Identifier(
            from_user_id=user_id,
            chat_id=chat_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
        )
        listeners = self.get_many_listeners_matching_with_identifier_pattern(
            pattern, listener_type
        )

        for listener in listeners:
            await self.stop_listener(listener)
