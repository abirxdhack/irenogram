
from typing import Union

import pyrogram
from pyrogram import raw

class ReadBusinessMessage:
    async def read_business_message(
        self: "pyrogram.Client",
        business_connection_id: str,
        chat_id: Union[int, str],
        message_id: int
    ) -> bool:
        """Marks a message as read on behalf of a managed business account.


        Parameters:
            business_connection_id (``str``): Unique identifier of the business connection.
            chat_id (``int`` | ``str``): Unique identifier of the chat.
            message_id (``int``): Identifier of the message to mark as read.

        Returns:
            ``bool``: True on success.
        """
        peer = await self.resolve_peer(chat_id)
        r = await self.invoke(
            raw.functions.InvokeWithBusinessConnection(
                connection_id=business_connection_id,
                query=raw.functions.messages.ReadHistory(
                    peer=peer,
                    max_id=message_id
                )
            )
        )
        return bool(r)
