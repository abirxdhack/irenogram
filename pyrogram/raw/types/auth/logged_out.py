
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class LoggedOut(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.auth.LoggedOut`.

    Details:
        - Layer: ``224``
        - ID: ``C3A2835F``

    Parameters:
        future_auth_token (``bytes``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.LogOut
    """

    __slots__: List[str] = ["future_auth_token"]

    ID = 0xc3a2835f
    QUALNAME = "types.auth.LoggedOut"

    def __init__(self, *, future_auth_token: Optional[bytes] = None) -> None:
        self.future_auth_token = future_auth_token

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LoggedOut":
        
        flags = Int.read(b)
        
        future_auth_token = Bytes.read(b) if flags & (1 << 0) else None
        return LoggedOut(future_auth_token=future_auth_token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.future_auth_token is not None else 0
        b.write(Int(flags))
        
        if self.future_auth_token is not None:
            b.write(Bytes(self.future_auth_token))
        
        return b.getvalue()
