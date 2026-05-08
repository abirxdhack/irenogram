


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputChatPhoto = Union[raw.types.InputChatPhoto, raw.types.InputChatPhotoEmpty, raw.types.InputChatUploadedPhoto]


class InputChatPhoto:
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputChatPhoto
            InputChatPhotoEmpty
            InputChatUploadedPhoto
    """

    QUALNAME = "pyrogram.raw.base.InputChatPhoto"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/input-chat-photo")
