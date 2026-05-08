
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InviteText(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.help.InviteText`.

    Details:
        - Layer: ``224``
        - ID: ``18CB9F78``

    Parameters:
        message (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetInviteText
    """

    __slots__: List[str] = ["message"]

    ID = 0x18cb9f78
    QUALNAME = "types.help.InviteText"

    def __init__(self, *, message: str) -> None:
        self.message = message

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InviteText":
        
        message = String.read(b)
        
        return InviteText(message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.message))
        
        return b.getvalue()
