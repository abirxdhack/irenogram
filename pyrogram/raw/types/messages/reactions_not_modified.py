
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ReactionsNotModified(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.Reactions`.

    Details:
        - Layer: ``224``
        - ID: ``B06FDBDF``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetTopReactions
            messages.GetRecentReactions
            messages.GetDefaultTagReactions
    """

    __slots__: List[str] = []

    ID = 0xb06fdbdf
    QUALNAME = "types.messages.ReactionsNotModified"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReactionsNotModified":
        
        return ReactionsNotModified()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
