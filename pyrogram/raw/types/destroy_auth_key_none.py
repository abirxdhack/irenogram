
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DestroyAuthKeyNone(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.DestroyAuthKeyRes`.

    Details:
        - Layer: ``224``
        - ID: ``0A9F2259``

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

    ID = 0x0a9f2259
    QUALNAME = "types.DestroyAuthKeyNone"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DestroyAuthKeyNone":
        
        return DestroyAuthKeyNone()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
