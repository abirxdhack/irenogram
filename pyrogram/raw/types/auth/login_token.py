
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class LoginToken(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.auth.LoginToken`.

    Details:
        - Layer: ``224``
        - ID: ``629F1980``

    Parameters:
        expires (``int`` ``32-bit``):
            N/A

        token (``bytes``):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.ExportLoginToken
            auth.ImportLoginToken
    """

    __slots__: List[str] = ["expires", "token"]

    ID = 0x629f1980
    QUALNAME = "types.auth.LoginToken"

    def __init__(self, *, expires: int, token: bytes) -> None:
        self.expires = expires
        self.token = token

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LoginToken":
        
        expires = Int.read(b)
        
        token = Bytes.read(b)
        
        return LoginToken(expires=expires, token=token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.expires))
        
        b.write(Bytes(self.token))
        
        return b.getvalue()
