
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class RpcAnswerDroppedRunning(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.RpcDropAnswer`.

    Details:
        - Layer: ``224``
        - ID: ``CD78E586``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            RpcDropAnswer
    """

    __slots__: List[str] = []

    ID = 0xcd78e586
    QUALNAME = "types.RpcAnswerDroppedRunning"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RpcAnswerDroppedRunning":
        
        return RpcAnswerDroppedRunning()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
