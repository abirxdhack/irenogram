
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class WebAuthorizations(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.account.WebAuthorizations`.

    Details:
        - Layer: ``224``
        - ID: ``ED56C9FC``

    Parameters:
        authorizations (List of :obj:`WebAuthorization <pyrogram.raw.base.WebAuthorization>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetWebAuthorizations
    """

    __slots__: List[str] = ["authorizations", "users"]

    ID = 0xed56c9fc
    QUALNAME = "types.account.WebAuthorizations"

    def __init__(self, *, authorizations: List["raw.base.WebAuthorization"], users: List["raw.base.User"]) -> None:
        self.authorizations = authorizations
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebAuthorizations":
        
        authorizations = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return WebAuthorizations(authorizations=authorizations, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.authorizations))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
