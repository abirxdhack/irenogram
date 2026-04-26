from typing import Optional

from pyrogram import raw, types

from ..object import Object


class UpgradedGiftAttributeId(Object):
    """This object contains identifier of an upgraded gift attribute to search for.

    It can be one of:

    - :obj:`~pyrogram.types.UpgradedfGiftAttributeIdModel`
    - :obj:`~pyrogram.types.UpgradedfGiftAttributeIdSymbol`
    - :obj:`~pyrogram.types.UpgradedfGiftAttributeIdBackdrop`
    """

    def __init__(
        self,
    ):
        super().__init__()

    @staticmethod
    def _parse(
        attribute_id: "raw.base.StarGiftAttributeId"
    ) -> Optional["UpgradedGiftAttributeId"]:
        if not attribute_id:
            return None

        if isinstance(attribute_id, raw.types.StarGiftAttributeIdModel):
            return types.UpgradedfGiftAttributeIdModel(
                sticker_id=attribute_id.document_id
            )
        elif isinstance(attribute_id, raw.types.StarGiftAttributeIdPattern):
            return types.UpgradedfGiftAttributeIdSymbol(
                sticker_id=attribute_id.document_id
            )
        elif isinstance(attribute_id, raw.types.StarGiftAttributeIdBackdrop):
            return types.UpgradedfGiftAttributeIdBackdrop(
                backdrop_id=attribute_id.backdrop_id
            )
