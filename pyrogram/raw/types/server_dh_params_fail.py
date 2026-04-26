
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ServerDHParamsFail(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ServerDHParams`.

    Details:
        - Layer: ``224``
        - ID: ``79CB045D``

    Parameters:
        nonce (``int`` ``128-bit``):
            N/A

        server_nonce (``int`` ``128-bit``):
            N/A

        new_nonce_hash (``int`` ``128-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            ReqDHParams
    """

    __slots__: List[str] = ["nonce", "server_nonce", "new_nonce_hash"]

    ID = 0x79cb045d
    QUALNAME = "types.ServerDHParamsFail"

    def __init__(self, *, nonce: int, server_nonce: int, new_nonce_hash: int) -> None:
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.new_nonce_hash = new_nonce_hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ServerDHParamsFail":
        
        nonce = Int128.read(b)
        
        server_nonce = Int128.read(b)
        
        new_nonce_hash = Int128.read(b)
        
        return ServerDHParamsFail(nonce=nonce, server_nonce=server_nonce, new_nonce_hash=new_nonce_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int128(self.nonce))
        
        b.write(Int128(self.server_nonce))
        
        b.write(Int128(self.new_nonce_hash))
        
        return b.getvalue()
