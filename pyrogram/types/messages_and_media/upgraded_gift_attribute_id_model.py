from pyrogram import raw

from .upgraded_gift_attribute_id import UpgradedGiftAttributeId


class UpgradedGiftAttributeIdModel(UpgradedGiftAttributeId):
    """Identifier of a gift model.

    Parameters:
        sticker_id (``int``):
            Identifier of the sticker representing the model.
    """
    def __init__(
        self,
        sticker_id: int,
    ):
        super().__init__()

        self.sticker_id = sticker_id

    def write(self) -> "raw.types.StarGiftAttributeIdModel":
        return raw.types.StarGiftAttributeIdModel(
            document_id=self.sticker_id
        )
