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


class InputMediaPaidMedia(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``224``
        - ID: ``C4103386``

    Parameters:
        stars_amount (``int`` ``64-bit``):
            N/A

        extended_media (List of :obj:`InputMedia <pyrogram.raw.base.InputMedia>`):
            N/A

        payload (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["stars_amount", "extended_media", "payload"]

    ID = 0xc4103386
    QUALNAME = "types.InputMediaPaidMedia"

    def __init__(self, *, stars_amount: int, extended_media: List["raw.base.InputMedia"], payload: Optional[str] = None) -> None:
        self.stars_amount = stars_amount  # long
        self.extended_media = extended_media  # Vector<InputMedia>
        self.payload = payload  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaPaidMedia":
        
        flags = Int.read(b)
        
        stars_amount = Long.read(b)
        
        extended_media = TLObject.read(b)
        
        payload = String.read(b) if flags & (1 << 0) else None
        return InputMediaPaidMedia(stars_amount=stars_amount, extended_media=extended_media, payload=payload)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.payload is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.stars_amount))
        
        b.write(Vector(self.extended_media))
        
        if self.payload is not None:
            b.write(String(self.payload))
        
        return b.getvalue()
