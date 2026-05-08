
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class TranslateResult(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.TranslatedText`.

    Details:
        - Layer: ``224``
        - ID: ``33DB32F8``

    Parameters:
        result (List of :obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.TranslateText
    """

    __slots__: List[str] = ["result"]

    ID = 0x33db32f8
    QUALNAME = "types.messages.TranslateResult"

    def __init__(self, *, result: List["raw.base.TextWithEntities"]) -> None:
        self.result = result

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TranslateResult":
        
        result = TLObject.read(b)
        
        return TranslateResult(result=result)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.result))
        
        return b.getvalue()
