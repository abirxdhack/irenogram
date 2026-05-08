
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EditStory(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``2C63A72B``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        id (``int`` ``32-bit``):
            N/A

        media (:obj:`InputMedia <pyrogram.raw.base.InputMedia>`, *optional*):
            N/A

        media_areas (List of :obj:`MediaArea <pyrogram.raw.base.MediaArea>`, *optional*):
            N/A

        caption (``str``, *optional*):
            N/A

        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            N/A

        privacy_rules (List of :obj:`InputPrivacyRule <pyrogram.raw.base.InputPrivacyRule>`, *optional*):
            N/A

        music (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "id", "media", "media_areas", "caption", "entities", "privacy_rules", "music"]

    ID = 0x2c63a72b
    QUALNAME = "functions.stories.EditStory"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int, media: "raw.base.InputMedia" = None, media_areas: Optional[List["raw.base.MediaArea"]] = None, caption: Optional[str] = None, entities: Optional[List["raw.base.MessageEntity"]] = None, privacy_rules: Optional[List["raw.base.InputPrivacyRule"]] = None, music: "raw.base.InputDocument" = None) -> None:
        self.peer = peer
        self.id = id
        self.media = media
        self.media_areas = media_areas
        self.caption = caption
        self.entities = entities
        self.privacy_rules = privacy_rules
        self.music = music

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditStory":
        
        flags = Int.read(b)
        
        peer = TLObject.read(b)
        
        id = Int.read(b)
        
        media = TLObject.read(b) if flags & (1 << 0) else None
        
        media_areas = TLObject.read(b) if flags & (1 << 3) else []
        
        caption = String.read(b) if flags & (1 << 1) else None
        entities = TLObject.read(b) if flags & (1 << 1) else []
        
        privacy_rules = TLObject.read(b) if flags & (1 << 2) else []
        
        music = TLObject.read(b) if flags & (1 << 4) else None
        
        return EditStory(peer=peer, id=id, media=media, media_areas=media_areas, caption=caption, entities=entities, privacy_rules=privacy_rules, music=music)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.media is not None else 0
        flags |= (1 << 3) if self.media_areas else 0
        flags |= (1 << 1) if self.caption is not None else 0
        flags |= (1 << 1) if self.entities else 0
        flags |= (1 << 2) if self.privacy_rules else 0
        flags |= (1 << 4) if self.music is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        if self.media is not None:
            b.write(self.media.write())
        
        if self.media_areas is not None:
            b.write(Vector(self.media_areas))
        
        if self.caption is not None:
            b.write(String(self.caption))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        if self.privacy_rules is not None:
            b.write(Vector(self.privacy_rules))
        
        if self.music is not None:
            b.write(self.music.write())
        
        return b.getvalue()
