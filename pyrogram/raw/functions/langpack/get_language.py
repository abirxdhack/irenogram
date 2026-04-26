
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetLanguage(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``6A596502``

    Parameters:
        lang_pack (``str``):
            N/A

        lang_code (``str``):
            N/A

    Returns:
        :obj:`LangPackLanguage <pyrogram.raw.base.LangPackLanguage>`
    """

    __slots__: List[str] = ["lang_pack", "lang_code"]

    ID = 0x6a596502
    QUALNAME = "functions.langpack.GetLanguage"

    def __init__(self, *, lang_pack: str, lang_code: str) -> None:
        self.lang_pack = lang_pack
        self.lang_code = lang_code

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetLanguage":
        
        lang_pack = String.read(b)
        
        lang_code = String.read(b)
        
        return GetLanguage(lang_pack=lang_pack, lang_code=lang_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.lang_pack))
        
        b.write(String(self.lang_code))
        
        return b.getvalue()
