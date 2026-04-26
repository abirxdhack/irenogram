
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateLangPackTooLong(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``46560264``

    Parameters:
        lang_code (``str``):
            N/A

    """

    __slots__: List[str] = ["lang_code"]

    ID = 0x46560264
    QUALNAME = "types.UpdateLangPackTooLong"

    def __init__(self, *, lang_code: str) -> None:
        self.lang_code = lang_code

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateLangPackTooLong":
        
        lang_code = String.read(b)
        
        return UpdateLangPackTooLong(lang_code=lang_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.lang_code))
        
        return b.getvalue()
