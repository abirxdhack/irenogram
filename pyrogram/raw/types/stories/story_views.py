
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class StoryViews(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.stories.StoryViews`.

    Details:
        - Layer: ``224``
        - ID: ``DE9EED1D``

    Parameters:
        views (List of :obj:`StoryViews <pyrogram.raw.base.StoryViews>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.GetStoriesViews
    """

    __slots__: List[str] = ["views", "users"]

    ID = 0xde9eed1d
    QUALNAME = "types.stories.StoryViews"

    def __init__(self, *, views: List["raw.base.StoryViews"], users: List["raw.base.User"]) -> None:
        self.views = views
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryViews":
        
        views = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return StoryViews(views=views, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.views))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
