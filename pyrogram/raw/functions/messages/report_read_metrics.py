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


class ReportReadMetrics(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``4067C5E6``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        metrics (List of :obj:`InputMessageReadMetric <pyrogram.raw.base.InputMessageReadMetric>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "metrics"]

    ID = 0x4067c5e6
    QUALNAME = "functions.messages.ReportReadMetrics"

    def __init__(self, *, peer: "raw.base.InputPeer", metrics: List["raw.base.InputMessageReadMetric"]) -> None:
        self.peer = peer  # InputPeer
        self.metrics = metrics  # Vector<InputMessageReadMetric>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportReadMetrics":
        # No flags
        
        peer = TLObject.read(b)
        
        metrics = TLObject.read(b)
        
        return ReportReadMetrics(peer=peer, metrics=metrics)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Vector(self.metrics))
        
        return b.getvalue()
