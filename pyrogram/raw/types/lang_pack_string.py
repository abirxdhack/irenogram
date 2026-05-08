
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class LangPackString(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.LangPackString`.

    Details:
        - Layer: ``224``
        - ID: ``CAD181F6``

    Parameters:
        key (``str``):
            N/A

        value (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            langpack.GetStrings
    """

    __slots__: List[str] = ["key", "value"]

    ID = 0xcad181f6
    QUALNAME = "types.LangPackString"

    def __init__(self, *, key: str, value: str) -> None:
        self.key = key
        self.value = value

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LangPackString":
        
        key = String.read(b)
        
        value = String.read(b)
        
        return LangPackString(key=key, value=value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.key))
        
        b.write(String(self.value))
        
        return b.getvalue()
