
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SentCodeSuccess(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.auth.SentCode`.

    Details:
        - Layer: ``224``
        - ID: ``2390FE44``

    Parameters:
        authorization (:obj:`auth.Authorization <pyrogram.raw.base.auth.Authorization>`):
            N/A

    Functions:
        This object can be returned by 7 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.SendCode
            auth.ResendCode
            auth.ResetLoginEmail
            auth.CheckPaidAuth
            account.SendChangePhoneCode
            account.SendConfirmPhoneCode
            account.SendVerifyPhoneCode
    """

    __slots__: List[str] = ["authorization"]

    ID = 0x2390fe44
    QUALNAME = "types.auth.SentCodeSuccess"

    def __init__(self, *, authorization: "raw.base.auth.Authorization") -> None:
        self.authorization = authorization

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodeSuccess":
        
        authorization = TLObject.read(b)
        
        return SentCodeSuccess(authorization=authorization)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.authorization.write())
        
        return b.getvalue()
