
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DestroySessionOk(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.DestroySessionRes`.

    Details:
        - Layer: ``224``
        - ID: ``E22045FC``

    Parameters:
        session_id (``int`` ``64-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            DestroySession
    """

    __slots__: List[str] = ["session_id"]

    ID = 0xe22045fc
    QUALNAME = "types.DestroySessionOk"

    def __init__(self, *, session_id: int) -> None:
        self.session_id = session_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DestroySessionOk":
        
        session_id = Long.read(b)
        
        return DestroySessionOk(session_id=session_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.session_id))
        
        return b.getvalue()
