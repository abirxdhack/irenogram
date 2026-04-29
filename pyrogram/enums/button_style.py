from enum import auto
from .auto_name import AutoName

class ButtonStyle(AutoName):
    """Visual style (colour) of an inline or reply keyboard button.

    Maps to ``KeyboardButtonStyle`` in the MTProto layer and ``ButtonStyle``
    in TDLib's ``td_api.tl``.
    """

    DEFAULT = auto()
    "No special colour (theme default)."

    PRIMARY = auto()
    "Dark-blue / accent colour."

    DANGER = auto()
    "Red (destructive actions)."

    SUCCESS = auto()
    "Green (confirmation actions)."
