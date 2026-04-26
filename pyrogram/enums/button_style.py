
from enum import auto
from .auto_name import AutoName

class ButtonStyle(AutoName):
    """Visual style (colour) of an inline or reply keyboard button.

    Maps to ``KeyboardButtonStyle`` in the MTProto layer and ``ButtonStyle``
    in TDLib's ``td_api.tl``.

    Attributes:
        DEFAULT: No special colour (theme default).
        PRIMARY: Dark-blue / accent colour.
        DANGER:  Red (destructive actions).
        SUCCESS: Green (confirmation actions).
    """

    DEFAULT = auto()
    PRIMARY = auto()
    DANGER  = auto()
    SUCCESS = auto()
