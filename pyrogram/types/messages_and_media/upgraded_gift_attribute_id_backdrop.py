from pyrogram import raw

from .upgraded_gift_attribute_id import UpgradedGiftAttributeId


class UpgradedGiftAttributeIdBackdrop(UpgradedGiftAttributeId):
    """Identifier of a gift backdrop.

    Parameters:
        backdrop_id (``int``):
            Identifier of the sticker representing the backdrop.
    """
    def __init__(
        self,
        backdrop_id: int,
    ):
        super().__init__()

        self.backdrop_id = backdrop_id

    def write(self) -> "raw.types.StarGiftAttributeIdBackdrop":
        return raw.types.StarGiftAttributeIdBackdrop(
            backdrop_id=self.backdrop_id
        )
