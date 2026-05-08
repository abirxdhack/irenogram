
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateInlineBotCallbackQuery(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``691E9052``

    Parameters:
        query_id (``int`` ``64-bit``):
            N/A

        user_id (``int`` ``64-bit``):
            N/A

        msg_id (:obj:`InputBotInlineMessageID <pyrogram.raw.base.InputBotInlineMessageID>`):
            N/A

        chat_instance (``int`` ``64-bit``):
            N/A

        data (``bytes``, *optional*):
            N/A

        game_short_name (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["query_id", "user_id", "msg_id", "chat_instance", "data", "game_short_name"]

    ID = 0x691e9052
    QUALNAME = "types.UpdateInlineBotCallbackQuery"

    def __init__(self, *, query_id: int, user_id: int, msg_id: "raw.base.InputBotInlineMessageID", chat_instance: int, data: Optional[bytes] = None, game_short_name: Optional[str] = None) -> None:
        self.query_id = query_id
        self.user_id = user_id
        self.msg_id = msg_id
        self.chat_instance = chat_instance
        self.data = data
        self.game_short_name = game_short_name

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateInlineBotCallbackQuery":
        
        flags = Int.read(b)
        
        query_id = Long.read(b)
        
        user_id = Long.read(b)
        
        msg_id = TLObject.read(b)
        
        chat_instance = Long.read(b)
        
        data = Bytes.read(b) if flags & (1 << 0) else None
        game_short_name = String.read(b) if flags & (1 << 1) else None
        return UpdateInlineBotCallbackQuery(query_id=query_id, user_id=user_id, msg_id=msg_id, chat_instance=chat_instance, data=data, game_short_name=game_short_name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.data is not None else 0
        flags |= (1 << 1) if self.game_short_name is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.query_id))
        
        b.write(Long(self.user_id))
        
        b.write(self.msg_id.write())
        
        b.write(Long(self.chat_instance))
        
        if self.data is not None:
            b.write(Bytes(self.data))
        
        if self.game_short_name is not None:
            b.write(String(self.game_short_name))
        
        return b.getvalue()
