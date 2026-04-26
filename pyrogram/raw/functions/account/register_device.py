
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class RegisterDevice(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``EC86017A``

    Parameters:
        token_type (``int`` ``32-bit``):
            N/A

        token (``str``):
            N/A

        app_sandbox (``bool``):
            N/A

        secret (``bytes``):
            N/A

        other_uids (List of ``int`` ``64-bit``):
            N/A

        no_muted (``bool``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["token_type", "token", "app_sandbox", "secret", "other_uids", "no_muted"]

    ID = 0xec86017a
    QUALNAME = "functions.account.RegisterDevice"

    def __init__(self, *, token_type: int, token: str, app_sandbox: bool, secret: bytes, other_uids: List[int], no_muted: Optional[bool] = None) -> None:
        self.token_type = token_type
        self.token = token
        self.app_sandbox = app_sandbox
        self.secret = secret
        self.other_uids = other_uids
        self.no_muted = no_muted

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RegisterDevice":
        
        flags = Int.read(b)
        
        no_muted = True if flags & (1 << 0) else False
        token_type = Int.read(b)
        
        token = String.read(b)
        
        app_sandbox = Bool.read(b)
        
        secret = Bytes.read(b)
        
        other_uids = TLObject.read(b, Long)
        
        return RegisterDevice(token_type=token_type, token=token, app_sandbox=app_sandbox, secret=secret, other_uids=other_uids, no_muted=no_muted)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.no_muted else 0
        b.write(Int(flags))
        
        b.write(Int(self.token_type))
        
        b.write(String(self.token))
        
        b.write(Bool(self.app_sandbox))
        
        b.write(Bytes(self.secret))
        
        b.write(Vector(self.other_uids, Long))
        
        return b.getvalue()
