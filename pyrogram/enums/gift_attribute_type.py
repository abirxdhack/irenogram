
from pyrogram import raw
from .auto_name import AutoName

class GiftAttributeType(AutoName):
    """Star gift attribute type enumeration used in :obj:`~pyrogram.types.GiftAttribute`."""

    MODEL = raw.types.StarGiftAttributeModel
    "Model attribute"

    SYMBOL = raw.types.StarGiftAttributePattern
    "Symbol attribute"

    BACKDROP = raw.types.StarGiftAttributeBackdrop
    "Backdrop attribute"

    ORIGINAL_DETAILS = raw.types.StarGiftAttributeOriginalDetails
    "Original details attribute"
