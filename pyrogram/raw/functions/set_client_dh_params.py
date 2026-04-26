
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SetClientDHParams(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``F5045F1F``

    Parameters:
        nonce (``int`` ``128-bit``):
            N/A

        server_nonce (``int`` ``128-bit``):
            N/A

        encrypted_data (``bytes``):
            N/A

    Returns:
        :obj:`SetClientDHParamsAnswer <pyrogram.raw.base.SetClientDHParamsAnswer>`
    """

    __slots__: List[str] = ["nonce", "server_nonce", "encrypted_data"]

    ID = 0xf5045f1f
    QUALNAME = "functions.SetClientDHParams"

    def __init__(self, *, nonce: int, server_nonce: int, encrypted_data: bytes) -> None:
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.encrypted_data = encrypted_data

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetClientDHParams":
        
        nonce = Int128.read(b)
        
        server_nonce = Int128.read(b)
        
        encrypted_data = Bytes.read(b)
        
        return SetClientDHParams(nonce=nonce, server_nonce=server_nonce, encrypted_data=encrypted_data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int128(self.nonce))
        
        b.write(Int128(self.server_nonce))
        
        b.write(Bytes(self.encrypted_data))
        
        return b.getvalue()
