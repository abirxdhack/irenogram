#  Pyrofork - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#  Copyright (C) 2022-present Mayuri-Chan <https://github.com/Mayuri-Chan>
#
#  This file is part of Pyrofork.
#
#  Pyrofork is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrofork is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrofork.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class MessageActionStarGiftPurchaseOffer(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``774278D4``

    Parameters:
        gift (:obj:`StarGift <pyrogram.raw.base.StarGift>`):
            N/A

        price (:obj:`StarsAmount <pyrogram.raw.base.StarsAmount>`):
            N/A

        expires_at (``int`` ``32-bit``):
            N/A

        accepted (``bool``, *optional*):
            N/A

        declined (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["gift", "price", "expires_at", "accepted", "declined"]

    ID = 0x774278d4
    QUALNAME = "types.MessageActionStarGiftPurchaseOffer"

    def __init__(self, *, gift: "raw.base.StarGift", price: "raw.base.StarsAmount", expires_at: int, accepted: Optional[bool] = None, declined: Optional[bool] = None) -> None:
        self.gift = gift  # StarGift
        self.price = price  # StarsAmount
        self.expires_at = expires_at  # int
        self.accepted = accepted  # flags.0?true
        self.declined = declined  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionStarGiftPurchaseOffer":
        
        flags = Int.read(b)
        
        accepted = True if flags & (1 << 0) else False
        declined = True if flags & (1 << 1) else False
        gift = TLObject.read(b)
        
        price = TLObject.read(b)
        
        expires_at = Int.read(b)
        
        return MessageActionStarGiftPurchaseOffer(gift=gift, price=price, expires_at=expires_at, accepted=accepted, declined=declined)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.accepted else 0
        flags |= (1 << 1) if self.declined else 0
        b.write(Int(flags))
        
        b.write(self.gift.write())
        
        b.write(self.price.write())
        
        b.write(Int(self.expires_at))
        
        return b.getvalue()
