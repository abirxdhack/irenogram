
from .auto_name import AutoName


class MaskPointType(AutoName):
    """Mask point type enumeration used in :obj:`~pyrogram.types.MaskPosition`."""

    FOREHEAD = 0
    "Mask point relative to the forehead."

    EYES = 1
    "Mask point relative to the eyes."

    MOUTH = 2
    "Mask point relative to the mouth."

    CHIN = 3
    "Mask point relative to the chin."
