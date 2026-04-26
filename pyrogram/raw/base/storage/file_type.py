


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

FileType = Union[raw.types.storage.FileGif, raw.types.storage.FileJpeg, raw.types.storage.FileMov, raw.types.storage.FileMp3, raw.types.storage.FileMp4, raw.types.storage.FilePartial, raw.types.storage.FilePdf, raw.types.storage.FilePng, raw.types.storage.FileUnknown, raw.types.storage.FileWebp]


class FileType:
    """Telegram API base type.

    Constructors:
        This base type has 10 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            storage.FileGif
            storage.FileJpeg
            storage.FileMov
            storage.FileMp3
            storage.FileMp4
            storage.FilePartial
            storage.FilePdf
            storage.FilePng
            storage.FileUnknown
            storage.FileWebp
    """

    QUALNAME = "pyrogram.raw.base.storage.FileType"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/file-type")
