


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputFileLocation = Union[raw.types.InputDocumentFileLocation, raw.types.InputEncryptedFileLocation, raw.types.InputFileLocation, raw.types.InputGroupCallStream, raw.types.InputPeerPhotoFileLocation, raw.types.InputPhotoFileLocation, raw.types.InputPhotoLegacyFileLocation, raw.types.InputSecureFileLocation, raw.types.InputStickerSetThumb, raw.types.InputTakeoutFileLocation]


class InputFileLocation:
    """Telegram API base type.

    Constructors:
        This base type has 10 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputDocumentFileLocation
            InputEncryptedFileLocation
            InputFileLocation
            InputGroupCallStream
            InputPeerPhotoFileLocation
            InputPhotoFileLocation
            InputPhotoLegacyFileLocation
            InputSecureFileLocation
            InputStickerSetThumb
            InputTakeoutFileLocation
    """

    QUALNAME = "pyrogram.raw.base.InputFileLocation"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/input-file-location")
