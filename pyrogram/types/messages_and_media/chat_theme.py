
from typing import Optional, TYPE_CHECKING

from ..object import Object
from pyrogram import raw

if TYPE_CHECKING:
    import pyrogram
    from pyrogram import types

class ChatTheme(Object):
    """A service message about a chat theme.

    parameters:
        emoticon (``str``):
            The emoticon of the chat theme.

        gift (:obj:`~pyrogram.types.Gift`, *optional*):
            Star gift that was used to change the chat theme.
            Only set for themes based on an upgraded unique gift.
    """

    def __init__(self, emoticon: Optional[str] = None, gift: Optional["types.Gift"] = None):
        super().__init__()
        self.emoticon = emoticon
        self.gift = gift

    @staticmethod
    async def _parse(
        client: "pyrogram.Client" = None,
        theme: "raw.base.ChatTheme" = None,
    ) -> Optional["ChatTheme"]:
        """Map a raw :obj:`raw.base.ChatTheme` value to :obj:`ChatTheme`.

        Accepts both :obj:`raw.types.ChatTheme` (an emoticon-based theme) and
        :obj:`raw.types.ChatThemeUniqueGift` (a theme backed by an upgraded gift).
        Returns ``None`` when *theme* is falsy.
        """
        if theme is None:
            return None

        from pyrogram import types

        if isinstance(theme, raw.types.ChatThemeUniqueGift):
            return ChatTheme(
                gift=await types.Gift._parse(client, theme.gift)
            )

        return ChatTheme(
            emoticon=getattr(theme, "emoticon", None)
        )
