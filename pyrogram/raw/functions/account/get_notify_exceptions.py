
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetNotifyExceptions(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``53577479``

    Parameters:
        compare_sound (``bool``, *optional*):
            N/A

        compare_stories (``bool``, *optional*):
            N/A

        peer (:obj:`InputNotifyPeer <pyrogram.raw.base.InputNotifyPeer>`, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["compare_sound", "compare_stories", "peer"]

    ID = 0x53577479
    QUALNAME = "functions.account.GetNotifyExceptions"

    def __init__(self, *, compare_sound: Optional[bool] = None, compare_stories: Optional[bool] = None, peer: "raw.base.InputNotifyPeer" = None) -> None:
        self.compare_sound = compare_sound
        self.compare_stories = compare_stories
        self.peer = peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetNotifyExceptions":
        
        flags = Int.read(b)
        
        compare_sound = True if flags & (1 << 1) else False
        compare_stories = True if flags & (1 << 2) else False
        peer = TLObject.read(b) if flags & (1 << 0) else None
        
        return GetNotifyExceptions(compare_sound=compare_sound, compare_stories=compare_stories, peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.compare_sound else 0
        flags |= (1 << 2) if self.compare_stories else 0
        flags |= (1 << 0) if self.peer is not None else 0
        b.write(Int(flags))
        
        if self.peer is not None:
            b.write(self.peer.write())
        
        return b.getvalue()
