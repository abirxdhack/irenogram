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


class BusinessWorkHours(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BusinessWorkHours`.

    Details:
        - Layer: ``224``
        - ID: ``8C92B098``

    Parameters:
        timezone_id (``str``):
            N/A

        weekly_open (List of :obj:`BusinessWeeklyOpen <pyrogram.raw.base.BusinessWeeklyOpen>`):
            N/A

        open_now (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["timezone_id", "weekly_open", "open_now"]

    ID = 0x8c92b098
    QUALNAME = "types.BusinessWorkHours"

    def __init__(self, *, timezone_id: str, weekly_open: List["raw.base.BusinessWeeklyOpen"], open_now: Optional[bool] = None) -> None:
        self.timezone_id = timezone_id  # string
        self.weekly_open = weekly_open  # Vector<BusinessWeeklyOpen>
        self.open_now = open_now  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BusinessWorkHours":
        
        flags = Int.read(b)
        
        open_now = True if flags & (1 << 0) else False
        timezone_id = String.read(b)
        
        weekly_open = TLObject.read(b)
        
        return BusinessWorkHours(timezone_id=timezone_id, weekly_open=weekly_open, open_now=open_now)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.open_now else 0
        b.write(Int(flags))
        
        b.write(String(self.timezone_id))
        
        b.write(Vector(self.weekly_open))
        
        return b.getvalue()
