
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputPrivacyValueDisallowUsers(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputPrivacyRule`.

    Details:
        - Layer: ``224``
        - ID: ``90110467``

    Parameters:
        users (List of :obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

    """

    __slots__: List[str] = ["users"]

    ID = 0x90110467
    QUALNAME = "types.InputPrivacyValueDisallowUsers"

    def __init__(self, *, users: List["raw.base.InputUser"]) -> None:
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPrivacyValueDisallowUsers":
        
        users = TLObject.read(b)
        
        return InputPrivacyValueDisallowUsers(users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.users))
        
        return b.getvalue()
