
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PremiumPromo(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.help.PremiumPromo`.

    Details:
        - Layer: ``224``
        - ID: ``5334759C``

    Parameters:
        status_text (``str``):
            N/A

        status_entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`):
            N/A

        video_sections (List of ``str``):
            N/A

        videos (List of :obj:`Document <pyrogram.raw.base.Document>`):
            N/A

        period_options (List of :obj:`PremiumSubscriptionOption <pyrogram.raw.base.PremiumSubscriptionOption>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetPremiumPromo
    """

    __slots__: List[str] = ["status_text", "status_entities", "video_sections", "videos", "period_options", "users"]

    ID = 0x5334759c
    QUALNAME = "types.help.PremiumPromo"

    def __init__(self, *, status_text: str, status_entities: List["raw.base.MessageEntity"], video_sections: List[str], videos: List["raw.base.Document"], period_options: List["raw.base.PremiumSubscriptionOption"], users: List["raw.base.User"]) -> None:
        self.status_text = status_text
        self.status_entities = status_entities
        self.video_sections = video_sections
        self.videos = videos
        self.period_options = period_options
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PremiumPromo":
        
        status_text = String.read(b)
        
        status_entities = TLObject.read(b)
        
        video_sections = TLObject.read(b, String)
        
        videos = TLObject.read(b)
        
        period_options = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return PremiumPromo(status_text=status_text, status_entities=status_entities, video_sections=video_sections, videos=videos, period_options=period_options, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.status_text))
        
        b.write(Vector(self.status_entities))
        
        b.write(Vector(self.video_sections, String))
        
        b.write(Vector(self.videos))
        
        b.write(Vector(self.period_options))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
