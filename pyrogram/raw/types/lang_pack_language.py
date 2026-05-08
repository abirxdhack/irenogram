
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class LangPackLanguage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.LangPackLanguage`.

    Details:
        - Layer: ``224``
        - ID: ``EECA5CE3``

    Parameters:
        name (``str``):
            N/A

        native_name (``str``):
            N/A

        lang_code (``str``):
            N/A

        plural_code (``str``):
            N/A

        strings_count (``int`` ``32-bit``):
            N/A

        translated_count (``int`` ``32-bit``):
            N/A

        translations_url (``str``):
            N/A

        official (``bool``, *optional*):
            N/A

        rtl (``bool``, *optional*):
            N/A

        beta (``bool``, *optional*):
            N/A

        base_lang_code (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            langpack.GetLanguages
            langpack.GetLanguage
    """

    __slots__: List[str] = ["name", "native_name", "lang_code", "plural_code", "strings_count", "translated_count", "translations_url", "official", "rtl", "beta", "base_lang_code"]

    ID = 0xeeca5ce3
    QUALNAME = "types.LangPackLanguage"

    def __init__(self, *, name: str, native_name: str, lang_code: str, plural_code: str, strings_count: int, translated_count: int, translations_url: str, official: Optional[bool] = None, rtl: Optional[bool] = None, beta: Optional[bool] = None, base_lang_code: Optional[str] = None) -> None:
        self.name = name
        self.native_name = native_name
        self.lang_code = lang_code
        self.plural_code = plural_code
        self.strings_count = strings_count
        self.translated_count = translated_count
        self.translations_url = translations_url
        self.official = official
        self.rtl = rtl
        self.beta = beta
        self.base_lang_code = base_lang_code

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LangPackLanguage":
        
        flags = Int.read(b)
        
        official = True if flags & (1 << 0) else False
        rtl = True if flags & (1 << 2) else False
        beta = True if flags & (1 << 3) else False
        name = String.read(b)
        
        native_name = String.read(b)
        
        lang_code = String.read(b)
        
        base_lang_code = String.read(b) if flags & (1 << 1) else None
        plural_code = String.read(b)
        
        strings_count = Int.read(b)
        
        translated_count = Int.read(b)
        
        translations_url = String.read(b)
        
        return LangPackLanguage(name=name, native_name=native_name, lang_code=lang_code, plural_code=plural_code, strings_count=strings_count, translated_count=translated_count, translations_url=translations_url, official=official, rtl=rtl, beta=beta, base_lang_code=base_lang_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.official else 0
        flags |= (1 << 2) if self.rtl else 0
        flags |= (1 << 3) if self.beta else 0
        flags |= (1 << 1) if self.base_lang_code is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.name))
        
        b.write(String(self.native_name))
        
        b.write(String(self.lang_code))
        
        if self.base_lang_code is not None:
            b.write(String(self.base_lang_code))
        
        b.write(String(self.plural_code))
        
        b.write(Int(self.strings_count))
        
        b.write(Int(self.translated_count))
        
        b.write(String(self.translations_url))
        
        return b.getvalue()
