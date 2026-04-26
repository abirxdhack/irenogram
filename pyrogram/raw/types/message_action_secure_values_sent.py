
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageActionSecureValuesSent(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``D95C6154``

    Parameters:
        types (List of :obj:`SecureValueType <pyrogram.raw.base.SecureValueType>`):
            N/A

    """

    __slots__: List[str] = ["types"]

    ID = 0xd95c6154
    QUALNAME = "types.MessageActionSecureValuesSent"

    def __init__(self, *, types: List["raw.base.SecureValueType"]) -> None:
        self.types = types

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionSecureValuesSent":
        
        types = TLObject.read(b)
        
        return MessageActionSecureValuesSent(types=types)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.types))
        
        return b.getvalue()
