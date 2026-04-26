
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class StoryItem(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StoryItem`.

    Details:
        - Layer: ``224``
        - ID: ``16A4B93C``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        expire_date (``int`` ``32-bit``):
            N/A

        media (:obj:`MessageMedia <pyrogram.raw.base.MessageMedia>`):
            N/A

        pinned (``bool``, *optional*):
            N/A

        public (``bool``, *optional*):
            N/A

        close_friends (``bool``, *optional*):
            N/A

        min (``bool``, *optional*):
            N/A

        noforwards (``bool``, *optional*):
            N/A

        edited (``bool``, *optional*):
            N/A

        contacts (``bool``, *optional*):
            N/A

        selected_contacts (``bool``, *optional*):
            N/A

        out (``bool``, *optional*):
            N/A

        from_id (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

        fwd_from (:obj:`StoryFwdHeader <pyrogram.raw.base.StoryFwdHeader>`, *optional*):
            N/A

        caption (``str``, *optional*):
            N/A

        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            N/A

        media_areas (List of :obj:`MediaArea <pyrogram.raw.base.MediaArea>`, *optional*):
            N/A

        privacy (List of :obj:`PrivacyRule <pyrogram.raw.base.PrivacyRule>`, *optional*):
            N/A

        views (:obj:`StoryViews <pyrogram.raw.base.StoryViews>`, *optional*):
            N/A

        sent_reaction (:obj:`Reaction <pyrogram.raw.base.Reaction>`, *optional*):
            N/A

        albums (List of ``int`` ``32-bit``, *optional*):
            N/A

        music (:obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "date", "expire_date", "media", "pinned", "public", "close_friends", "min", "noforwards", "edited", "contacts", "selected_contacts", "out", "from_id", "fwd_from", "caption", "entities", "media_areas", "privacy", "views", "sent_reaction", "albums", "music"]

    ID = 0x16a4b93c
    QUALNAME = "types.StoryItem"

    def __init__(self, *, id: int, date: int, expire_date: int, media: "raw.base.MessageMedia", pinned: Optional[bool] = None, public: Optional[bool] = None, close_friends: Optional[bool] = None, min: Optional[bool] = None, noforwards: Optional[bool] = None, edited: Optional[bool] = None, contacts: Optional[bool] = None, selected_contacts: Optional[bool] = None, out: Optional[bool] = None, from_id: "raw.base.Peer" = None, fwd_from: "raw.base.StoryFwdHeader" = None, caption: Optional[str] = None, entities: Optional[List["raw.base.MessageEntity"]] = None, media_areas: Optional[List["raw.base.MediaArea"]] = None, privacy: Optional[List["raw.base.PrivacyRule"]] = None, views: "raw.base.StoryViews" = None, sent_reaction: "raw.base.Reaction" = None, albums: Optional[List[int]] = None, music: "raw.base.Document" = None) -> None:
        self.id = id
        self.date = date
        self.expire_date = expire_date
        self.media = media
        self.pinned = pinned
        self.public = public
        self.close_friends = close_friends
        self.min = min
        self.noforwards = noforwards
        self.edited = edited
        self.contacts = contacts
        self.selected_contacts = selected_contacts
        self.out = out
        self.from_id = from_id
        self.fwd_from = fwd_from
        self.caption = caption
        self.entities = entities
        self.media_areas = media_areas
        self.privacy = privacy
        self.views = views
        self.sent_reaction = sent_reaction
        self.albums = albums
        self.music = music

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryItem":
        
        flags = Int.read(b)
        
        pinned = True if flags & (1 << 5) else False
        public = True if flags & (1 << 7) else False
        close_friends = True if flags & (1 << 8) else False
        min = True if flags & (1 << 9) else False
        noforwards = True if flags & (1 << 10) else False
        edited = True if flags & (1 << 11) else False
        contacts = True if flags & (1 << 12) else False
        selected_contacts = True if flags & (1 << 13) else False
        out = True if flags & (1 << 16) else False
        id = Int.read(b)
        
        date = Int.read(b)
        
        from_id = TLObject.read(b) if flags & (1 << 18) else None
        
        fwd_from = TLObject.read(b) if flags & (1 << 17) else None
        
        expire_date = Int.read(b)
        
        caption = String.read(b) if flags & (1 << 0) else None
        entities = TLObject.read(b) if flags & (1 << 1) else []
        
        media = TLObject.read(b)
        
        media_areas = TLObject.read(b) if flags & (1 << 14) else []
        
        privacy = TLObject.read(b) if flags & (1 << 2) else []
        
        views = TLObject.read(b) if flags & (1 << 3) else None
        
        sent_reaction = TLObject.read(b) if flags & (1 << 15) else None
        
        albums = TLObject.read(b, Int) if flags & (1 << 19) else []
        
        music = TLObject.read(b) if flags & (1 << 20) else None
        
        return StoryItem(id=id, date=date, expire_date=expire_date, media=media, pinned=pinned, public=public, close_friends=close_friends, min=min, noforwards=noforwards, edited=edited, contacts=contacts, selected_contacts=selected_contacts, out=out, from_id=from_id, fwd_from=fwd_from, caption=caption, entities=entities, media_areas=media_areas, privacy=privacy, views=views, sent_reaction=sent_reaction, albums=albums, music=music)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.pinned else 0
        flags |= (1 << 7) if self.public else 0
        flags |= (1 << 8) if self.close_friends else 0
        flags |= (1 << 9) if self.min else 0
        flags |= (1 << 10) if self.noforwards else 0
        flags |= (1 << 11) if self.edited else 0
        flags |= (1 << 12) if self.contacts else 0
        flags |= (1 << 13) if self.selected_contacts else 0
        flags |= (1 << 16) if self.out else 0
        flags |= (1 << 18) if self.from_id is not None else 0
        flags |= (1 << 17) if self.fwd_from is not None else 0
        flags |= (1 << 0) if self.caption is not None else 0
        flags |= (1 << 1) if self.entities else 0
        flags |= (1 << 14) if self.media_areas else 0
        flags |= (1 << 2) if self.privacy else 0
        flags |= (1 << 3) if self.views is not None else 0
        flags |= (1 << 15) if self.sent_reaction is not None else 0
        flags |= (1 << 19) if self.albums else 0
        flags |= (1 << 20) if self.music is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(Int(self.date))
        
        if self.from_id is not None:
            b.write(self.from_id.write())
        
        if self.fwd_from is not None:
            b.write(self.fwd_from.write())
        
        b.write(Int(self.expire_date))
        
        if self.caption is not None:
            b.write(String(self.caption))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        b.write(self.media.write())
        
        if self.media_areas is not None:
            b.write(Vector(self.media_areas))
        
        if self.privacy is not None:
            b.write(Vector(self.privacy))
        
        if self.views is not None:
            b.write(self.views.write())
        
        if self.sent_reaction is not None:
            b.write(self.sent_reaction.write())
        
        if self.albums is not None:
            b.write(Vector(self.albums, Int))
        
        if self.music is not None:
            b.write(self.music.write())
        
        return b.getvalue()
