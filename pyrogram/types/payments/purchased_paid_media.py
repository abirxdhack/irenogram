
from pyrogram import raw, types

from ..object import Object

class PurchasedPaidMedia(Object):
    """This object represents information about purchased paid media.


    Parameters:
        from_user (:obj:`~pyrogram.types.User`):
            User who bought the paid media.

        payload (``str``):
            Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.
    """

    def __init__(
        self,
        from_user: "types.User",
        payload: str
    ):
        super().__init__()

        self.from_user = from_user
        self.payload = payload

    @staticmethod
    def _parse(client, purchased_media: "raw.types.UpdateBotPurchasedPaidMedia", users) -> "PurchasedPaidMedia":
        return PurchasedPaidMedia(
            from_user=types.User._parse(client, users.get(purchased_media.user_id)),
            payload=purchased_media.payload
        )
