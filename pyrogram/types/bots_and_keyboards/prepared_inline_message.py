
from datetime import datetime
from ..object import Object

class PreparedInlineMessage(Object):
    """Describes an inline message to be sent by a user of a Mini App.


    Parameters:
        inline_message_id (``str``):
            Unique identifier of the prepared message.

        expiration_date (:py:obj:`~datetime.datetime`):
            Expiration date of the prepared message.
    """

    def __init__(
        self,
        *,
        inline_message_id: str,
        expiration_date: datetime
    ):
        super().__init__()
        self.inline_message_id = inline_message_id
        self.expiration_date = expiration_date

    @staticmethod
    def _parse(r) -> "PreparedInlineMessage":
        return PreparedInlineMessage(
            inline_message_id=r.id,
            expiration_date=datetime.utcfromtimestamp(r.expire_date)
        )
