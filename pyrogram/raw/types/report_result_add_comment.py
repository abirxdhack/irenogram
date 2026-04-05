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


class ReportResultAddComment(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ReportResult`.

    Details:
        - Layer: ``224``
        - ID: ``6F09AC31``

    Parameters:
        option (``bytes``):
            N/A

        optional (``bool``, *optional*):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.Report
            stories.Report
    """

    __slots__: List[str] = ["option", "optional"]

    ID = 0x6f09ac31
    QUALNAME = "types.ReportResultAddComment"

    def __init__(self, *, option: bytes, optional: Optional[bool] = None) -> None:
        self.option = option  # bytes
        self.optional = optional  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportResultAddComment":
        
        flags = Int.read(b)
        
        optional = True if flags & (1 << 0) else False
        option = Bytes.read(b)
        
        return ReportResultAddComment(option=option, optional=optional)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.optional else 0
        b.write(Int(flags))
        
        b.write(Bytes(self.option))
        
        return b.getvalue()
