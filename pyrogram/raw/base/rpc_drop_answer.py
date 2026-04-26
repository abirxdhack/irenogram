


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

RpcDropAnswer = Union[raw.types.RpcAnswerDropped, raw.types.RpcAnswerDroppedRunning, raw.types.RpcAnswerUnknown]


class RpcDropAnswer:
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            RpcAnswerDropped
            RpcAnswerDroppedRunning
            RpcAnswerUnknown

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            RpcDropAnswer
    """

    QUALNAME = "pyrogram.raw.base.RpcDropAnswer"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/rpc-drop-answer")
