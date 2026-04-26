
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DestroyAuthKeyOk(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.DestroyAuthKeyRes`.

    Details:
        - Layer: ``224``
        - ID: ``F660E1D4``

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

    ID = 0xf660e1d4
    QUALNAME = "types.DestroyAuthKeyOk"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DestroyAuthKeyOk":
        
        return DestroyAuthKeyOk()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
