
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class AvailableReactionsNotModified(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.AvailableReactions`.

    Details:
        - Layer: ``224``
        - ID: ``9F071957``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAvailableReactions
    """

    __slots__: List[str] = []

    ID = 0x9f071957
    QUALNAME = "types.messages.AvailableReactionsNotModified"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AvailableReactionsNotModified":
        
        return AvailableReactionsNotModified()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
