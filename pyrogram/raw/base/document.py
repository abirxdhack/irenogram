


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

Document = Union[raw.types.Document, raw.types.DocumentEmpty]


class Document:
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            Document
            DocumentEmpty

    Functions:
        This object can be returned by 4 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.UploadTheme
            account.UploadRingtone
            messages.GetDocumentByHash
            messages.GetCustomEmojiDocuments
    """

    QUALNAME = "pyrogram.raw.base.Document"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/document")
