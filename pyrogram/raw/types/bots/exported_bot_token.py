
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ExportedBotToken(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.bots.ExportedBotToken`.

    Details:
        - Layer: ``224``
        - ID: ``3C60B621``

    Parameters:
        token (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.ExportBotToken
    """

    __slots__: List[str] = ["token"]

    ID = 0x3c60b621
    QUALNAME = "types.bots.ExportedBotToken"

    def __init__(self, *, token: str) -> None:
        self.token = token

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedBotToken":
        
        token = String.read(b)
        
        return ExportedBotToken(token=token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.token))
        
        return b.getvalue()
