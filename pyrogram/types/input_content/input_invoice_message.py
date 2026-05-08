
from typing import Union

import pyrogram
from pyrogram import raw

from .input_invoice import InputInvoice


class InputInvoiceMessage(InputInvoice):
    """An invoice from a message or paid media purchase from paid media message.

    Parameters:
        chat_id (``int`` | ``str``):
            Unique identifier (int) or username (str) of the target chat.

        message_id (``int``):
            Unique message identifier.
    """
    def __init__(
        self,
        chat_id: Union[int, str],
        message_id: int,
    ):
        super().__init__()

        self.chat_id = chat_id
        self.message_id = message_id

    async def write(self, client: "pyrogram.Client"):
        return raw.types.InputInvoiceMessage(
            peer=await client.resolve_peer(self.chat_id),
            msg_id=self.message_id
        )
