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


class MediaAreaCoordinates(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MediaAreaCoordinates`.

    Details:
        - Layer: ``224``
        - ID: ``CFC9E002``

    Parameters:
        x (``float`` ``64-bit``):
            N/A

        y (``float`` ``64-bit``):
            N/A

        w (``float`` ``64-bit``):
            N/A

        h (``float`` ``64-bit``):
            N/A

        rotation (``float`` ``64-bit``):
            N/A

        radius (``float`` ``64-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["x", "y", "w", "h", "rotation", "radius"]

    ID = 0xcfc9e002
    QUALNAME = "types.MediaAreaCoordinates"

    def __init__(self, *, x: float, y: float, w: float, h: float, rotation: float, radius: Optional[float] = None) -> None:
        self.x = x  # double
        self.y = y  # double
        self.w = w  # double
        self.h = h  # double
        self.rotation = rotation  # double
        self.radius = radius  # flags.0?double

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MediaAreaCoordinates":
        
        flags = Int.read(b)
        
        x = Double.read(b)
        
        y = Double.read(b)
        
        w = Double.read(b)
        
        h = Double.read(b)
        
        rotation = Double.read(b)
        
        radius = Double.read(b) if flags & (1 << 0) else None
        return MediaAreaCoordinates(x=x, y=y, w=w, h=h, rotation=rotation, radius=radius)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.radius is not None else 0
        b.write(Int(flags))
        
        b.write(Double(self.x))
        
        b.write(Double(self.y))
        
        b.write(Double(self.w))
        
        b.write(Double(self.h))
        
        b.write(Double(self.rotation))
        
        if self.radius is not None:
            b.write(Double(self.radius))
        
        return b.getvalue()
