
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UserInfoEmpty(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.help.UserInfo`.

    Details:
        - Layer: ``224``
        - ID: ``F3AE2EED``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetUserInfo
            help.EditUserInfo
    """

    __slots__: List[str] = []

    ID = 0xf3ae2eed
    QUALNAME = "types.help.UserInfoEmpty"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UserInfoEmpty":
        
        return UserInfoEmpty()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
