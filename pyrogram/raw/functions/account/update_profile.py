
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateProfile(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``78515775``

    Parameters:
        first_name (``str``, *optional*):
            N/A

        last_name (``str``, *optional*):
            N/A

        about (``str``, *optional*):
            N/A

    Returns:
        :obj:`User <pyrogram.raw.base.User>`
    """

    __slots__: List[str] = ["first_name", "last_name", "about"]

    ID = 0x78515775
    QUALNAME = "functions.account.UpdateProfile"

    def __init__(self, *, first_name: Optional[str] = None, last_name: Optional[str] = None, about: Optional[str] = None) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.about = about

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateProfile":
        
        flags = Int.read(b)
        
        first_name = String.read(b) if flags & (1 << 0) else None
        last_name = String.read(b) if flags & (1 << 1) else None
        about = String.read(b) if flags & (1 << 2) else None
        return UpdateProfile(first_name=first_name, last_name=last_name, about=about)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.first_name is not None else 0
        flags |= (1 << 1) if self.last_name is not None else 0
        flags |= (1 << 2) if self.about is not None else 0
        b.write(Int(flags))
        
        if self.first_name is not None:
            b.write(String(self.first_name))
        
        if self.last_name is not None:
            b.write(String(self.last_name))
        
        if self.about is not None:
            b.write(String(self.about))
        
        return b.getvalue()
