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


class GetStarsGiftOptions(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``D3C96BC8``

    Parameters:
        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`, *optional*):
            N/A

    Returns:
        List of :obj:`StarsGiftOption <pyrogram.raw.base.StarsGiftOption>`
    """

    __slots__: List[str] = ["user_id"]

    ID = 0xd3c96bc8
    QUALNAME = "functions.payments.GetStarsGiftOptions"

    def __init__(self, *, user_id: "raw.base.InputUser" = None) -> None:
        self.user_id = user_id  # flags.0?InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStarsGiftOptions":
        
        flags = Int.read(b)
        
        user_id = TLObject.read(b) if flags & (1 << 0) else None
        
        return GetStarsGiftOptions(user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.user_id is not None else 0
        b.write(Int(flags))
        
        if self.user_id is not None:
            b.write(self.user_id.write())
        
        return b.getvalue()
