
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageActionSecureValuesSentMe(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``1B287353``

    Parameters:
        values (List of :obj:`SecureValue <pyrogram.raw.base.SecureValue>`):
            N/A

        credentials (:obj:`SecureCredentialsEncrypted <pyrogram.raw.base.SecureCredentialsEncrypted>`):
            N/A

    """

    __slots__: List[str] = ["values", "credentials"]

    ID = 0x1b287353
    QUALNAME = "types.MessageActionSecureValuesSentMe"

    def __init__(self, *, values: List["raw.base.SecureValue"], credentials: "raw.base.SecureCredentialsEncrypted") -> None:
        self.values = values
        self.credentials = credentials

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionSecureValuesSentMe":
        
        values = TLObject.read(b)
        
        credentials = TLObject.read(b)
        
        return MessageActionSecureValuesSentMe(values=values, credentials=credentials)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.values))
        
        b.write(self.credentials.write())
        
        return b.getvalue()
