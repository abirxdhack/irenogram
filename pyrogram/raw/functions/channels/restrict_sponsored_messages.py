
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class RestrictSponsoredMessages(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``9AE91519``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        restricted (``bool``):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "restricted"]

    ID = 0x9ae91519
    QUALNAME = "functions.channels.RestrictSponsoredMessages"

    def __init__(self, *, channel: "raw.base.InputChannel", restricted: bool) -> None:
        self.channel = channel
        self.restricted = restricted

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RestrictSponsoredMessages":
        
        channel = TLObject.read(b)
        
        restricted = Bool.read(b)
        
        return RestrictSponsoredMessages(channel=channel, restricted=restricted)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.channel.write())
        
        b.write(Bool(self.restricted))
        
        return b.getvalue()
