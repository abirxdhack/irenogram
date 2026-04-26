
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UniqueStarGift(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.UniqueStarGift`.

    Details:
        - Layer: ``224``
        - ID: ``416C56E8``

    Parameters:
        gift (:obj:`StarGift <pyrogram.raw.base.StarGift>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetUniqueStarGift
    """

    __slots__: List[str] = ["gift", "chats", "users"]

    ID = 0x416c56e8
    QUALNAME = "types.payments.UniqueStarGift"

    def __init__(self, *, gift: "raw.base.StarGift", chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.gift = gift
        self.chats = chats
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UniqueStarGift":
        
        gift = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return UniqueStarGift(gift=gift, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.gift.write())
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
