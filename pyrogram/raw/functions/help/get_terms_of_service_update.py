
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetTermsOfServiceUpdate(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``2CA51FD1``

    Parameters:
        No parameters required.

    Returns:
        :obj:`help.TermsOfServiceUpdate <pyrogram.raw.base.help.TermsOfServiceUpdate>`
    """

    __slots__: List[str] = []

    ID = 0x2ca51fd1
    QUALNAME = "functions.help.GetTermsOfServiceUpdate"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetTermsOfServiceUpdate":
        
        return GetTermsOfServiceUpdate()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
