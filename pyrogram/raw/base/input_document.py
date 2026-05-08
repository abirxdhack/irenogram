


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputDocument = Union[raw.types.InputDocument, raw.types.InputDocumentEmpty]


class InputDocument:
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputDocument
            InputDocumentEmpty
    """

    QUALNAME = "pyrogram.raw.base.InputDocument"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/input-document")
