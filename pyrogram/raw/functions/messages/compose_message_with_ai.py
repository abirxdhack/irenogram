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


class ComposeMessageWithAI(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``FD426AFE``

    Parameters:
        text (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`):
            N/A

        proofread (``bool``, *optional*):
            N/A

        emojify (``bool``, *optional*):
            N/A

        translate_to_lang (``str``, *optional*):
            N/A

        change_tone (``str``, *optional*):
            N/A

    Returns:
        :obj:`messages.ComposedMessageWithAI <pyrogram.raw.base.messages.ComposedMessageWithAI>`
    """

    __slots__: List[str] = ["text", "proofread", "emojify", "translate_to_lang", "change_tone"]

    ID = 0xfd426afe
    QUALNAME = "functions.messages.ComposeMessageWithAI"

    def __init__(self, *, text: "raw.base.TextWithEntities", proofread: Optional[bool] = None, emojify: Optional[bool] = None, translate_to_lang: Optional[str] = None, change_tone: Optional[str] = None) -> None:
        self.text = text  # TextWithEntities
        self.proofread = proofread  # flags.0?true
        self.emojify = emojify  # flags.3?true
        self.translate_to_lang = translate_to_lang  # flags.1?string
        self.change_tone = change_tone  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ComposeMessageWithAI":
        
        flags = Int.read(b)
        
        proofread = True if flags & (1 << 0) else False
        emojify = True if flags & (1 << 3) else False
        text = TLObject.read(b)
        
        translate_to_lang = String.read(b) if flags & (1 << 1) else None
        change_tone = String.read(b) if flags & (1 << 2) else None
        return ComposeMessageWithAI(text=text, proofread=proofread, emojify=emojify, translate_to_lang=translate_to_lang, change_tone=change_tone)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.proofread else 0
        flags |= (1 << 3) if self.emojify else 0
        flags |= (1 << 1) if self.translate_to_lang is not None else 0
        flags |= (1 << 2) if self.change_tone is not None else 0
        b.write(Int(flags))
        
        b.write(self.text.write())
        
        if self.translate_to_lang is not None:
            b.write(String(self.translate_to_lang))
        
        if self.change_tone is not None:
            b.write(String(self.change_tone))
        
        return b.getvalue()
