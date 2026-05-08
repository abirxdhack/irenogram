from pyrogram import raw

from .upgraded_gift_attribute_id import UpgradedGiftAttributeId


class UpgradedGiftAttributeIdSymbol(UpgradedGiftAttributeId):
    """Identifier of a gift symbol.

    Parameters:
        sticker_id (``int``):
            Identifier of the sticker representing the symbol.
    """
    def __init__(
        self,
        sticker_id: int,
    ):
        super().__init__()

        self.sticker_id = sticker_id

    def write(self) -> "raw.types.StarGiftAttributeIdPattern":
        return raw.types.StarGiftAttributeIdPattern(
            document_id=self.sticker_id
        )
