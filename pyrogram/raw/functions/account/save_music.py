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


class SaveMusic(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``B26732A9``

    Parameters:
        id (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`):
            N/A

        unsave (``bool``, *optional*):
            N/A

        after_id (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id", "unsave", "after_id"]

    ID = 0xb26732a9
    QUALNAME = "functions.account.SaveMusic"

    def __init__(self, *, id: "raw.base.InputDocument", unsave: Optional[bool] = None, after_id: "raw.base.InputDocument" = None) -> None:
        self.id = id  # InputDocument
        self.unsave = unsave  # flags.0?true
        self.after_id = after_id  # flags.1?InputDocument

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveMusic":
        
        flags = Int.read(b)
        
        unsave = True if flags & (1 << 0) else False
        id = TLObject.read(b)
        
        after_id = TLObject.read(b) if flags & (1 << 1) else None
        
        return SaveMusic(id=id, unsave=unsave, after_id=after_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.unsave else 0
        flags |= (1 << 1) if self.after_id is not None else 0
        b.write(Int(flags))
        
        b.write(self.id.write())
        
        if self.after_id is not None:
            b.write(self.after_id.write())
        
        return b.getvalue()
