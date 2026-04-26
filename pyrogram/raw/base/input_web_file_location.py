


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputWebFileLocation = Union[raw.types.InputWebFileAudioAlbumThumbLocation, raw.types.InputWebFileGeoPointLocation, raw.types.InputWebFileLocation]


class InputWebFileLocation:
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputWebFileAudioAlbumThumbLocation
            InputWebFileGeoPointLocation
            InputWebFileLocation
    """

    QUALNAME = "pyrogram.raw.base.InputWebFileLocation"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/input-web-file-location")
