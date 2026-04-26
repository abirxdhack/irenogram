
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class BusinessGreetingMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BusinessGreetingMessage`.

    Details:
        - Layer: ``224``
        - ID: ``E519ABAB``

    Parameters:
        shortcut_id (``int`` ``32-bit``):
            N/A

        recipients (:obj:`BusinessRecipients <pyrogram.raw.base.BusinessRecipients>`):
            N/A

        no_activity_days (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["shortcut_id", "recipients", "no_activity_days"]

    ID = 0xe519abab
    QUALNAME = "types.BusinessGreetingMessage"

    def __init__(self, *, shortcut_id: int, recipients: "raw.base.BusinessRecipients", no_activity_days: int) -> None:
        self.shortcut_id = shortcut_id
        self.recipients = recipients
        self.no_activity_days = no_activity_days

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BusinessGreetingMessage":
        
        shortcut_id = Int.read(b)
        
        recipients = TLObject.read(b)
        
        no_activity_days = Int.read(b)
        
        return BusinessGreetingMessage(shortcut_id=shortcut_id, recipients=recipients, no_activity_days=no_activity_days)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.shortcut_id))
        
        b.write(self.recipients.write())
        
        b.write(Int(self.no_activity_days))
        
        return b.getvalue()
