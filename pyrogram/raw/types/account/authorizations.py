
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class Authorizations(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.account.Authorizations`.

    Details:
        - Layer: ``224``
        - ID: ``4BFF8EA0``

    Parameters:
        authorization_ttl_days (``int`` ``32-bit``):
            N/A

        authorizations (List of :obj:`Authorization <pyrogram.raw.base.Authorization>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetAuthorizations
    """

    __slots__: List[str] = ["authorization_ttl_days", "authorizations"]

    ID = 0x4bff8ea0
    QUALNAME = "types.account.Authorizations"

    def __init__(self, *, authorization_ttl_days: int, authorizations: List["raw.base.Authorization"]) -> None:
        self.authorization_ttl_days = authorization_ttl_days
        self.authorizations = authorizations

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Authorizations":
        
        authorization_ttl_days = Int.read(b)
        
        authorizations = TLObject.read(b)
        
        return Authorizations(authorization_ttl_days=authorization_ttl_days, authorizations=authorizations)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.authorization_ttl_days))
        
        b.write(Vector(self.authorizations))
        
        return b.getvalue()
