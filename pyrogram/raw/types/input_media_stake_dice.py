
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputMediaStakeDice(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``224``
        - ID: ``F3A9244A``

    Parameters:
        game_hash (``str``):
            N/A

        ton_amount (``int`` ``64-bit``):
            N/A

        client_seed (``bytes``):
            N/A

    """

    __slots__: List[str] = ["game_hash", "ton_amount", "client_seed"]

    ID = 0xf3a9244a
    QUALNAME = "types.InputMediaStakeDice"

    def __init__(self, *, game_hash: str, ton_amount: int, client_seed: bytes) -> None:
        self.game_hash = game_hash
        self.ton_amount = ton_amount
        self.client_seed = client_seed

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaStakeDice":
        
        game_hash = String.read(b)
        
        ton_amount = Long.read(b)
        
        client_seed = Bytes.read(b)
        
        return InputMediaStakeDice(game_hash=game_hash, ton_amount=ton_amount, client_seed=client_seed)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.game_hash))
        
        b.write(Long(self.ton_amount))
        
        b.write(Bytes(self.client_seed))
        
        return b.getvalue()
