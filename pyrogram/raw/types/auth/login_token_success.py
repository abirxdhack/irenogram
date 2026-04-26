
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class LoginTokenSuccess(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.auth.LoginToken`.

    Details:
        - Layer: ``224``
        - ID: ``390D5C5E``

    Parameters:
        authorization (:obj:`auth.Authorization <pyrogram.raw.base.auth.Authorization>`):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.ExportLoginToken
            auth.ImportLoginToken
    """

    __slots__: List[str] = ["authorization"]

    ID = 0x390d5c5e
    QUALNAME = "types.auth.LoginTokenSuccess"

    def __init__(self, *, authorization: "raw.base.auth.Authorization") -> None:
        self.authorization = authorization

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LoginTokenSuccess":
        
        authorization = TLObject.read(b)
        
        return LoginTokenSuccess(authorization=authorization)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.authorization.write())
        
        return b.getvalue()
