
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateLangPack(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``56022F4D``

    Parameters:
        difference (:obj:`LangPackDifference <pyrogram.raw.base.LangPackDifference>`):
            N/A

    """

    __slots__: List[str] = ["difference"]

    ID = 0x56022f4d
    QUALNAME = "types.UpdateLangPack"

    def __init__(self, *, difference: "raw.base.LangPackDifference") -> None:
        self.difference = difference

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateLangPack":
        
        difference = TLObject.read(b)
        
        return UpdateLangPack(difference=difference)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.difference.write())
        
        return b.getvalue()
