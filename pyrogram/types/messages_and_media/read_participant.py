
import pyrogram
from pyrogram import raw, utils
from datetime import datetime
from ..object import Object

class ReadParticipant(Object):
    """Contains information about a read participant.


    Parameters:
        user (:obj:`~pyrogram.types.User`):
            User who read the message.

        date (:py:obj:`~datetime.datetime`):
            Date the message was read.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        user_id: "pyrogram.types.User",
        date: "datetime"
    ):
        super().__init__(client)

        self.user = user_id
        self.date = date

    @staticmethod
    async def _parse(
        client,
        read_participant: "raw.base.ReadParticipantDate"
    ) -> "ReadParticipant":
        return ReadParticipant(
            client=client,
            user_id=await client.get_users(read_participant.user_id),
            date=utils.timestamp_to_datetime(read_participant.date)
        )
