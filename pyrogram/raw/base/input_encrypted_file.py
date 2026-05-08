


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputEncryptedFile = Union[raw.types.InputEncryptedFile, raw.types.InputEncryptedFileBigUploaded, raw.types.InputEncryptedFileEmpty, raw.types.InputEncryptedFileUploaded]


class InputEncryptedFile:
    """Telegram API base type.

    Constructors:
        This base type has 4 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputEncryptedFile
            InputEncryptedFileBigUploaded
            InputEncryptedFileEmpty
            InputEncryptedFileUploaded
    """

    QUALNAME = "pyrogram.raw.base.InputEncryptedFile"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/input-encrypted-file")
