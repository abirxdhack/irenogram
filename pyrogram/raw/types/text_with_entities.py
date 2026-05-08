
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class TextWithEntities(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.TextWithEntities`.

    Details:
        - Layer: ``224``
        - ID: ``751F3146``

    Parameters:
        text (``str``):
            N/A

        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.SummarizeText
    """

    __slots__: List[str] = ["text", "entities"]

    ID = 0x751f3146
    QUALNAME = "types.TextWithEntities"

    def __init__(self, *, text: str, entities: List["raw.base.MessageEntity"]) -> None:
        self.text = text
        self.entities = entities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TextWithEntities":
        
        text = String.read(b)
        
        entities = TLObject.read(b)
        
        return TextWithEntities(text=text, entities=entities)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.text))
        
        b.write(Vector(self.entities))
        
        return b.getvalue()
