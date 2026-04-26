
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class AttachMenuBotsNotModified(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.AttachMenuBots`.

    Details:
        - Layer: ``224``
        - ID: ``F1D88A5C``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAttachMenuBots
    """

    __slots__: List[str] = []

    ID = 0xf1d88a5c
    QUALNAME = "types.AttachMenuBotsNotModified"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AttachMenuBotsNotModified":
        
        return AttachMenuBotsNotModified()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
