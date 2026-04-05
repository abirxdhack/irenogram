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


class TimezonesList(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.help.TimezonesList`.

    Details:
        - Layer: ``224``
        - ID: ``7B74ED71``

    Parameters:
        timezones (List of :obj:`Timezone <pyrogram.raw.base.Timezone>`):
            N/A

        hash (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetTimezonesList
    """

    __slots__: List[str] = ["timezones", "hash"]

    ID = 0x7b74ed71
    QUALNAME = "types.help.TimezonesList"

    def __init__(self, *, timezones: List["raw.base.Timezone"], hash: int) -> None:
        self.timezones = timezones  # Vector<Timezone>
        self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TimezonesList":
        # No flags
        
        timezones = TLObject.read(b)
        
        hash = Int.read(b)
        
        return TimezonesList(timezones=timezones, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.timezones))
        
        b.write(Int(self.hash))
        
        return b.getvalue()
