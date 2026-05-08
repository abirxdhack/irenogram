
import pyrogram

from ..object import Object
from pyrogram import raw, types

class ChatWallpaper(Object):
    """A service message about a chat wallpaper.

    parameters:
        wallpaper (:obj:`types.Wallpaper`):
            The chat wallpaper.

        is_same (``bool``, *optional*):
            True, if the chat wallpaper is the same as the previous one.

        is_both (``bool``, *optional*):
            True, if the chat wallpaper is for both side.
    """

    def __init__(
        self,
        wallpaper: "types.Wallpaper",
        is_same: bool = None,
        is_both: bool = None
    ):
        super().__init__()
        self.wallpaper = wallpaper
        self.is_same = is_same
        self.is_both = is_both

    @staticmethod
    def _parse(client: "pyrogram.Client", chat_wallpaper: "raw.types.ChatWallpaper") -> "ChatWallpaper":
        return ChatWallpaper(
            wallpaper=types.Wallpaper._parse(client, chat_wallpaper.wallpaper),
            is_same=getattr(chat_wallpaper, "is_same", None),
            is_both=getattr(chat_wallpaper, "is_both", None)
        )
