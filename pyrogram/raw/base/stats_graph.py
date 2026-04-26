


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

StatsGraph = Union[raw.types.StatsGraph, raw.types.StatsGraphAsync, raw.types.StatsGraphError]


class StatsGraph:
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            StatsGraph
            StatsGraphAsync
            StatsGraphError

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stats.LoadAsyncGraph
    """

    QUALNAME = "pyrogram.raw.base.StatsGraph"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/stats-graph")
