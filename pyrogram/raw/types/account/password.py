
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class Password(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.account.Password`.

    Details:
        - Layer: ``224``
        - ID: ``957B50FB``

    Parameters:
        new_algo (:obj:`PasswordKdfAlgo <pyrogram.raw.base.PasswordKdfAlgo>`):
            N/A

        new_secure_algo (:obj:`SecurePasswordKdfAlgo <pyrogram.raw.base.SecurePasswordKdfAlgo>`):
            N/A

        secure_random (``bytes``):
            N/A

        has_recovery (``bool``, *optional*):
            N/A

        has_secure_values (``bool``, *optional*):
            N/A

        has_password (``bool``, *optional*):
            N/A

        current_algo (:obj:`PasswordKdfAlgo <pyrogram.raw.base.PasswordKdfAlgo>`, *optional*):
            N/A

        srp_B (``bytes``, *optional*):
            N/A

        srp_id (``int`` ``64-bit``, *optional*):
            N/A

        hint (``str``, *optional*):
            N/A

        email_unconfirmed_pattern (``str``, *optional*):
            N/A

        pending_reset_date (``int`` ``32-bit``, *optional*):
            N/A

        login_email_pattern (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetPassword
    """

    __slots__: List[str] = ["new_algo", "new_secure_algo", "secure_random", "has_recovery", "has_secure_values", "has_password", "current_algo", "srp_B", "srp_id", "hint", "email_unconfirmed_pattern", "pending_reset_date", "login_email_pattern"]

    ID = 0x957b50fb
    QUALNAME = "types.account.Password"

    def __init__(self, *, new_algo: "raw.base.PasswordKdfAlgo", new_secure_algo: "raw.base.SecurePasswordKdfAlgo", secure_random: bytes, has_recovery: Optional[bool] = None, has_secure_values: Optional[bool] = None, has_password: Optional[bool] = None, current_algo: "raw.base.PasswordKdfAlgo" = None, srp_B: Optional[bytes] = None, srp_id: Optional[int] = None, hint: Optional[str] = None, email_unconfirmed_pattern: Optional[str] = None, pending_reset_date: Optional[int] = None, login_email_pattern: Optional[str] = None) -> None:
        self.new_algo = new_algo
        self.new_secure_algo = new_secure_algo
        self.secure_random = secure_random
        self.has_recovery = has_recovery
        self.has_secure_values = has_secure_values
        self.has_password = has_password
        self.current_algo = current_algo
        self.srp_B = srp_B
        self.srp_id = srp_id
        self.hint = hint
        self.email_unconfirmed_pattern = email_unconfirmed_pattern
        self.pending_reset_date = pending_reset_date
        self.login_email_pattern = login_email_pattern

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Password":
        
        flags = Int.read(b)
        
        has_recovery = True if flags & (1 << 0) else False
        has_secure_values = True if flags & (1 << 1) else False
        has_password = True if flags & (1 << 2) else False
        current_algo = TLObject.read(b) if flags & (1 << 2) else None
        
        srp_B = Bytes.read(b) if flags & (1 << 2) else None
        srp_id = Long.read(b) if flags & (1 << 2) else None
        hint = String.read(b) if flags & (1 << 3) else None
        email_unconfirmed_pattern = String.read(b) if flags & (1 << 4) else None
        new_algo = TLObject.read(b)
        
        new_secure_algo = TLObject.read(b)
        
        secure_random = Bytes.read(b)
        
        pending_reset_date = Int.read(b) if flags & (1 << 5) else None
        login_email_pattern = String.read(b) if flags & (1 << 6) else None
        return Password(new_algo=new_algo, new_secure_algo=new_secure_algo, secure_random=secure_random, has_recovery=has_recovery, has_secure_values=has_secure_values, has_password=has_password, current_algo=current_algo, srp_B=srp_B, srp_id=srp_id, hint=hint, email_unconfirmed_pattern=email_unconfirmed_pattern, pending_reset_date=pending_reset_date, login_email_pattern=login_email_pattern)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.has_recovery else 0
        flags |= (1 << 1) if self.has_secure_values else 0
        flags |= (1 << 2) if self.has_password else 0
        flags |= (1 << 2) if self.current_algo is not None else 0
        flags |= (1 << 2) if self.srp_B is not None else 0
        flags |= (1 << 2) if self.srp_id is not None else 0
        flags |= (1 << 3) if self.hint is not None else 0
        flags |= (1 << 4) if self.email_unconfirmed_pattern is not None else 0
        flags |= (1 << 5) if self.pending_reset_date is not None else 0
        flags |= (1 << 6) if self.login_email_pattern is not None else 0
        b.write(Int(flags))
        
        if self.current_algo is not None:
            b.write(self.current_algo.write())
        
        if self.srp_B is not None:
            b.write(Bytes(self.srp_B))
        
        if self.srp_id is not None:
            b.write(Long(self.srp_id))
        
        if self.hint is not None:
            b.write(String(self.hint))
        
        if self.email_unconfirmed_pattern is not None:
            b.write(String(self.email_unconfirmed_pattern))
        
        b.write(self.new_algo.write())
        
        b.write(self.new_secure_algo.write())
        
        b.write(Bytes(self.secure_random))
        
        if self.pending_reset_date is not None:
            b.write(Int(self.pending_reset_date))
        
        if self.login_email_pattern is not None:
            b.write(String(self.login_email_pattern))
        
        return b.getvalue()
