


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputFile = Union[raw.types.InputFile, raw.types.InputFileBig, raw.types.InputFileStoryDocument]


class InputFile:
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputFile
            InputFileBig
            InputFileStoryDocument
    """

    QUALNAME = "pyrogram.raw.base.InputFile"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/input-file")
