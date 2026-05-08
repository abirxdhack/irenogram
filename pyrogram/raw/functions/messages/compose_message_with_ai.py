
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ComposeMessageWithAI(TLObject):
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
        self.text = text
        self.proofread = proofread
        self.emojify = emojify
        self.translate_to_lang = translate_to_lang
        self.change_tone = change_tone

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
