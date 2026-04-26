
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DestroyAuthKeyFail(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.DestroyAuthKeyRes`.

    Details:
        - Layer: ``224``
        - ID: ``EA109B13``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            DestroyAuthKey
    """

    __slots__: List[str] = []

    ID = 0xea109b13
    QUALNAME = "types.DestroyAuthKeyFail"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DestroyAuthKeyFail":
        
        return DestroyAuthKeyFail()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
