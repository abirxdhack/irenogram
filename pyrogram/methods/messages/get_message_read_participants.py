
import pyrogram

from pyrogram import types
from typing import Union

class GetMessageReadParticipants:
    async def get_message_read_participants(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int
    ):
        """Get the list of users who have read a message.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                You can also use chat public link in form of *t.me/<username>* (str).

            message_id (``int``):
                Unique identifier of the target message.

        Returns:
            ``AsyncGenerator``: On success, an async generator yielding :obj:`~pyrogram.types.ReadParticipant` objects is returned.
        """

        peer = await self.resolve_peer(chat_id)
        r = await self.invoke(
            pyrogram.raw.functions.messages.GetMessageReadParticipants(
                peer=peer,
                msg_id=message_id
            )
        )
        for read_participant in r:
            yield await types.ReadParticipant._parse(
                client=self,
                read_participant=read_participant
            )
