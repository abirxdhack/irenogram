
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PrivacyRules(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.account.PrivacyRules`.

    Details:
        - Layer: ``224``
        - ID: ``50A04E45``

    Parameters:
        rules (List of :obj:`PrivacyRule <pyrogram.raw.base.PrivacyRule>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetPrivacy
            account.SetPrivacy
    """

    __slots__: List[str] = ["rules", "chats", "users"]

    ID = 0x50a04e45
    QUALNAME = "types.account.PrivacyRules"

    def __init__(self, *, rules: List["raw.base.PrivacyRule"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.rules = rules
        self.chats = chats
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PrivacyRules":
        
        rules = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return PrivacyRules(rules=rules, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.rules))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
