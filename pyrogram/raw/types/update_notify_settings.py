
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateNotifySettings(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``BEC268EF``

    Parameters:
        peer (:obj:`NotifyPeer <pyrogram.raw.base.NotifyPeer>`):
            N/A

        notify_settings (:obj:`PeerNotifySettings <pyrogram.raw.base.PeerNotifySettings>`):
            N/A

    """

    __slots__: List[str] = ["peer", "notify_settings"]

    ID = 0xbec268ef
    QUALNAME = "types.UpdateNotifySettings"

    def __init__(self, *, peer: "raw.base.NotifyPeer", notify_settings: "raw.base.PeerNotifySettings") -> None:
        self.peer = peer
        self.notify_settings = notify_settings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateNotifySettings":
        
        peer = TLObject.read(b)
        
        notify_settings = TLObject.read(b)
        
        return UpdateNotifySettings(peer=peer, notify_settings=notify_settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(self.notify_settings.write())
        
        return b.getvalue()
