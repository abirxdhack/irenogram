
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ResetPasswordOk(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.account.ResetPasswordResult`.

    Details:
        - Layer: ``224``
        - ID: ``E926D63E``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.ResetPassword
    """

    __slots__: List[str] = []

    ID = 0xe926d63e
    QUALNAME = "types.account.ResetPasswordOk"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResetPasswordOk":
        
        return ResetPasswordOk()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
