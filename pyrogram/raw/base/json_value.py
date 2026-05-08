


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

JSONValue = Union[raw.types.JsonArray, raw.types.JsonBool, raw.types.JsonNull, raw.types.JsonNumber, raw.types.JsonObject, raw.types.JsonString]


class JSONValue:
    """Telegram API base type.

    Constructors:
        This base type has 6 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            JsonArray
            JsonBool
            JsonNull
            JsonNumber
            JsonObject
            JsonString
    """

    QUALNAME = "pyrogram.raw.base.JSONValue"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/json-value")
