
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class StarsStatus(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.StarsStatus`.

    Details:
        - Layer: ``224``
        - ID: ``6C9CE8ED``

    Parameters:
        balance (:obj:`StarsAmount <pyrogram.raw.base.StarsAmount>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        subscriptions (List of :obj:`StarsSubscription <pyrogram.raw.base.StarsSubscription>`, *optional*):
            N/A

        subscriptions_next_offset (``str``, *optional*):
            N/A

        subscriptions_missing_balance (``int`` ``64-bit``, *optional*):
            N/A

        history (List of :obj:`StarsTransaction <pyrogram.raw.base.StarsTransaction>`, *optional*):
            N/A

        next_offset (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 4 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetStarsStatus
            payments.GetStarsTransactions
            payments.GetStarsTransactionsByID
            payments.GetStarsSubscriptions
    """

    __slots__: List[str] = ["balance", "chats", "users", "subscriptions", "subscriptions_next_offset", "subscriptions_missing_balance", "history", "next_offset"]

    ID = 0x6c9ce8ed
    QUALNAME = "types.payments.StarsStatus"

    def __init__(self, *, balance: "raw.base.StarsAmount", chats: List["raw.base.Chat"], users: List["raw.base.User"], subscriptions: Optional[List["raw.base.StarsSubscription"]] = None, subscriptions_next_offset: Optional[str] = None, subscriptions_missing_balance: Optional[int] = None, history: Optional[List["raw.base.StarsTransaction"]] = None, next_offset: Optional[str] = None) -> None:
        self.balance = balance
        self.chats = chats
        self.users = users
        self.subscriptions = subscriptions
        self.subscriptions_next_offset = subscriptions_next_offset
        self.subscriptions_missing_balance = subscriptions_missing_balance
        self.history = history
        self.next_offset = next_offset

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarsStatus":
        
        flags = Int.read(b)
        
        balance = TLObject.read(b)
        
        subscriptions = TLObject.read(b) if flags & (1 << 1) else []
        
        subscriptions_next_offset = String.read(b) if flags & (1 << 2) else None
        subscriptions_missing_balance = Long.read(b) if flags & (1 << 4) else None
        history = TLObject.read(b) if flags & (1 << 3) else []
        
        next_offset = String.read(b) if flags & (1 << 0) else None
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return StarsStatus(balance=balance, chats=chats, users=users, subscriptions=subscriptions, subscriptions_next_offset=subscriptions_next_offset, subscriptions_missing_balance=subscriptions_missing_balance, history=history, next_offset=next_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.subscriptions else 0
        flags |= (1 << 2) if self.subscriptions_next_offset is not None else 0
        flags |= (1 << 4) if self.subscriptions_missing_balance is not None else 0
        flags |= (1 << 3) if self.history else 0
        flags |= (1 << 0) if self.next_offset is not None else 0
        b.write(Int(flags))
        
        b.write(self.balance.write())
        
        if self.subscriptions is not None:
            b.write(Vector(self.subscriptions))
        
        if self.subscriptions_next_offset is not None:
            b.write(String(self.subscriptions_next_offset))
        
        if self.subscriptions_missing_balance is not None:
            b.write(Long(self.subscriptions_missing_balance))
        
        if self.history is not None:
            b.write(Vector(self.history))
        
        if self.next_offset is not None:
            b.write(String(self.next_offset))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
