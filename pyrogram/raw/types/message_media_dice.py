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


class MessageMediaDice(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``224``
        - ID: ``8CBEC07``

    Parameters:
        value (``int`` ``32-bit``):
            N/A

        emoticon (``str``):
            N/A

        game_outcome (:obj:`messages.EmojiGameOutcome <pyrogram.raw.base.messages.EmojiGameOutcome>`, *optional*):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: List[str] = ["value", "emoticon", "game_outcome"]

    ID = 0x8cbec07
    QUALNAME = "types.MessageMediaDice"

    def __init__(self, *, value: int, emoticon: str, game_outcome: "raw.base.messages.EmojiGameOutcome" = None) -> None:
        self.value = value  # int
        self.emoticon = emoticon  # string
        self.game_outcome = game_outcome  # flags.0?messages.EmojiGameOutcome

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaDice":
        
        flags = Int.read(b)
        
        value = Int.read(b)
        
        emoticon = String.read(b)
        
        game_outcome = TLObject.read(b) if flags & (1 << 0) else None
        
        return MessageMediaDice(value=value, emoticon=emoticon, game_outcome=game_outcome)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.game_outcome is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.value))
        
        b.write(String(self.emoticon))
        
        if self.game_outcome is not None:
            b.write(self.game_outcome.write())
        
        return b.getvalue()
