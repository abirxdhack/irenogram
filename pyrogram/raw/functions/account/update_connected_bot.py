
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateConnectedBot(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``66A08C7E``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        recipients (:obj:`InputBusinessBotRecipients <pyrogram.raw.base.InputBusinessBotRecipients>`):
            N/A

        deleted (``bool``, *optional*):
            N/A

        rights (:obj:`BusinessBotRights <pyrogram.raw.base.BusinessBotRights>`, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["bot", "recipients", "deleted", "rights"]

    ID = 0x66a08c7e
    QUALNAME = "functions.account.UpdateConnectedBot"

    def __init__(self, *, bot: "raw.base.InputUser", recipients: "raw.base.InputBusinessBotRecipients", deleted: Optional[bool] = None, rights: "raw.base.BusinessBotRights" = None) -> None:
        self.bot = bot
        self.recipients = recipients
        self.deleted = deleted
        self.rights = rights

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateConnectedBot":
        
        flags = Int.read(b)
        
        deleted = True if flags & (1 << 1) else False
        rights = TLObject.read(b) if flags & (1 << 0) else None
        
        bot = TLObject.read(b)
        
        recipients = TLObject.read(b)
        
        return UpdateConnectedBot(bot=bot, recipients=recipients, deleted=deleted, rights=rights)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.deleted else 0
        flags |= (1 << 0) if self.rights is not None else 0
        b.write(Int(flags))
        
        if self.rights is not None:
            b.write(self.rights.write())
        
        b.write(self.bot.write())
        
        b.write(self.recipients.write())
        
        return b.getvalue()
