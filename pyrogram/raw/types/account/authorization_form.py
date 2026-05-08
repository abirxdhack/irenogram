
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class AuthorizationForm(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.account.AuthorizationForm`.

    Details:
        - Layer: ``224``
        - ID: ``AD2E1CD8``

    Parameters:
        required_types (List of :obj:`SecureRequiredType <pyrogram.raw.base.SecureRequiredType>`):
            N/A

        values (List of :obj:`SecureValue <pyrogram.raw.base.SecureValue>`):
            N/A

        errors (List of :obj:`SecureValueError <pyrogram.raw.base.SecureValueError>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        privacy_policy_url (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetAuthorizationForm
    """

    __slots__: List[str] = ["required_types", "values", "errors", "users", "privacy_policy_url"]

    ID = 0xad2e1cd8
    QUALNAME = "types.account.AuthorizationForm"

    def __init__(self, *, required_types: List["raw.base.SecureRequiredType"], values: List["raw.base.SecureValue"], errors: List["raw.base.SecureValueError"], users: List["raw.base.User"], privacy_policy_url: Optional[str] = None) -> None:
        self.required_types = required_types
        self.values = values
        self.errors = errors
        self.users = users
        self.privacy_policy_url = privacy_policy_url

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AuthorizationForm":
        
        flags = Int.read(b)
        
        required_types = TLObject.read(b)
        
        values = TLObject.read(b)
        
        errors = TLObject.read(b)
        
        users = TLObject.read(b)
        
        privacy_policy_url = String.read(b) if flags & (1 << 0) else None
        return AuthorizationForm(required_types=required_types, values=values, errors=errors, users=users, privacy_policy_url=privacy_policy_url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.privacy_policy_url is not None else 0
        b.write(Int(flags))
        
        b.write(Vector(self.required_types))
        
        b.write(Vector(self.values))
        
        b.write(Vector(self.errors))
        
        b.write(Vector(self.users))
        
        if self.privacy_policy_url is not None:
            b.write(String(self.privacy_policy_url))
        
        return b.getvalue()
