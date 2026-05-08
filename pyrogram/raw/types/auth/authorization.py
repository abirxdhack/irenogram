
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class Authorization(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.auth.Authorization`.

    Details:
        - Layer: ``224``
        - ID: ``2EA2C0D4``

    Parameters:
        user (:obj:`User <pyrogram.raw.base.User>`):
            N/A

        setup_password_required (``bool``, *optional*):
            N/A

        otherwise_relogin_days (``int`` ``32-bit``, *optional*):
            N/A

        tmp_sessions (``int`` ``32-bit``, *optional*):
            N/A

        future_auth_token (``bytes``, *optional*):
            N/A

    Functions:
        This object can be returned by 8 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.SignUp
            auth.SignIn
            auth.ImportAuthorization
            auth.ImportBotAuthorization
            auth.CheckPassword
            auth.RecoverPassword
            auth.ImportWebTokenAuthorization
            auth.FinishPasskeyLogin
    """

    __slots__: List[str] = ["user", "setup_password_required", "otherwise_relogin_days", "tmp_sessions", "future_auth_token"]

    ID = 0x2ea2c0d4
    QUALNAME = "types.auth.Authorization"

    def __init__(self, *, user: "raw.base.User", setup_password_required: Optional[bool] = None, otherwise_relogin_days: Optional[int] = None, tmp_sessions: Optional[int] = None, future_auth_token: Optional[bytes] = None) -> None:
        self.user = user
        self.setup_password_required = setup_password_required
        self.otherwise_relogin_days = otherwise_relogin_days
        self.tmp_sessions = tmp_sessions
        self.future_auth_token = future_auth_token

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Authorization":
        
        flags = Int.read(b)
        
        setup_password_required = True if flags & (1 << 1) else False
        otherwise_relogin_days = Int.read(b) if flags & (1 << 1) else None
        tmp_sessions = Int.read(b) if flags & (1 << 0) else None
        future_auth_token = Bytes.read(b) if flags & (1 << 2) else None
        user = TLObject.read(b)
        
        return Authorization(user=user, setup_password_required=setup_password_required, otherwise_relogin_days=otherwise_relogin_days, tmp_sessions=tmp_sessions, future_auth_token=future_auth_token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.setup_password_required else 0
        flags |= (1 << 1) if self.otherwise_relogin_days is not None else 0
        flags |= (1 << 0) if self.tmp_sessions is not None else 0
        flags |= (1 << 2) if self.future_auth_token is not None else 0
        b.write(Int(flags))
        
        if self.otherwise_relogin_days is not None:
            b.write(Int(self.otherwise_relogin_days))
        
        if self.tmp_sessions is not None:
            b.write(Int(self.tmp_sessions))
        
        if self.future_auth_token is not None:
            b.write(Bytes(self.future_auth_token))
        
        b.write(self.user.write())
        
        return b.getvalue()
