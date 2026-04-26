
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SendGroupCallEncryptedMessage(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``E5AFA56D``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

        encrypted_message (``bytes``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["call", "encrypted_message"]

    ID = 0xe5afa56d
    QUALNAME = "functions.phone.SendGroupCallEncryptedMessage"

    def __init__(self, *, call: "raw.base.InputGroupCall", encrypted_message: bytes) -> None:
        self.call = call
        self.encrypted_message = encrypted_message

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendGroupCallEncryptedMessage":
        
        call = TLObject.read(b)
        
        encrypted_message = Bytes.read(b)
        
        return SendGroupCallEncryptedMessage(call=call, encrypted_message=encrypted_message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.call.write())
        
        b.write(Bytes(self.encrypted_message))
        
        return b.getvalue()
