
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SuggestBirthday(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``FC533372``

    Parameters:
        id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        birthday (:obj:`Birthday <pyrogram.raw.base.Birthday>`):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["id", "birthday"]

    ID = 0xfc533372
    QUALNAME = "functions.users.SuggestBirthday"

    def __init__(self, *, id: "raw.base.InputUser", birthday: "raw.base.Birthday") -> None:
        self.id = id
        self.birthday = birthday

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SuggestBirthday":
        
        id = TLObject.read(b)
        
        birthday = TLObject.read(b)
        
        return SuggestBirthday(id=id, birthday=birthday)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.id.write())
        
        b.write(self.birthday.write())
        
        return b.getvalue()
