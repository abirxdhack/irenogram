
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputThemeSettings(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputThemeSettings`.

    Details:
        - Layer: ``224``
        - ID: ``8FDE504F``

    Parameters:
        base_theme (:obj:`BaseTheme <pyrogram.raw.base.BaseTheme>`):
            N/A

        accent_color (``int`` ``32-bit``):
            N/A

        message_colors_animated (``bool``, *optional*):
            N/A

        outbox_accent_color (``int`` ``32-bit``, *optional*):
            N/A

        message_colors (List of ``int`` ``32-bit``, *optional*):
            N/A

        wallpaper (:obj:`InputWallPaper <pyrogram.raw.base.InputWallPaper>`, *optional*):
            N/A

        wallpaper_settings (:obj:`WallPaperSettings <pyrogram.raw.base.WallPaperSettings>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["base_theme", "accent_color", "message_colors_animated", "outbox_accent_color", "message_colors", "wallpaper", "wallpaper_settings"]

    ID = 0x8fde504f
    QUALNAME = "types.InputThemeSettings"

    def __init__(self, *, base_theme: "raw.base.BaseTheme", accent_color: int, message_colors_animated: Optional[bool] = None, outbox_accent_color: Optional[int] = None, message_colors: Optional[List[int]] = None, wallpaper: "raw.base.InputWallPaper" = None, wallpaper_settings: "raw.base.WallPaperSettings" = None) -> None:
        self.base_theme = base_theme
        self.accent_color = accent_color
        self.message_colors_animated = message_colors_animated
        self.outbox_accent_color = outbox_accent_color
        self.message_colors = message_colors
        self.wallpaper = wallpaper
        self.wallpaper_settings = wallpaper_settings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputThemeSettings":
        
        flags = Int.read(b)
        
        message_colors_animated = True if flags & (1 << 2) else False
        base_theme = TLObject.read(b)
        
        accent_color = Int.read(b)
        
        outbox_accent_color = Int.read(b) if flags & (1 << 3) else None
        message_colors = TLObject.read(b, Int) if flags & (1 << 0) else []
        
        wallpaper = TLObject.read(b) if flags & (1 << 1) else None
        
        wallpaper_settings = TLObject.read(b) if flags & (1 << 1) else None
        
        return InputThemeSettings(base_theme=base_theme, accent_color=accent_color, message_colors_animated=message_colors_animated, outbox_accent_color=outbox_accent_color, message_colors=message_colors, wallpaper=wallpaper, wallpaper_settings=wallpaper_settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.message_colors_animated else 0
        flags |= (1 << 3) if self.outbox_accent_color is not None else 0
        flags |= (1 << 0) if self.message_colors else 0
        flags |= (1 << 1) if self.wallpaper is not None else 0
        flags |= (1 << 1) if self.wallpaper_settings is not None else 0
        b.write(Int(flags))
        
        b.write(self.base_theme.write())
        
        b.write(Int(self.accent_color))
        
        if self.outbox_accent_color is not None:
            b.write(Int(self.outbox_accent_color))
        
        if self.message_colors is not None:
            b.write(Vector(self.message_colors, Int))
        
        if self.wallpaper is not None:
            b.write(self.wallpaper.write())
        
        if self.wallpaper_settings is not None:
            b.write(self.wallpaper_settings.write())
        
        return b.getvalue()
