
from ..object import Object
from pyrogram import raw

class WallpaperSettings(Object):
    """A wallpaper settings.

    parameters:
        is_blur (``bool``, *optional*):
            True, if the wallpaper is blurred.

        is_motion (``bool``, *optional*):
            True, if the wallpaper is motion.

        background_color (``int``, *optional*):
            The background color of the wallpaper.

        second_background_color (``int``, *optional*):
            The second background color of the wallpaper.

        third_background_color (``int``, *optional*):
            The third background color of the wallpaper.

        fourth_background_color (``int``, *optional*):
            The fourth background color of the wallpaper.

        intensity (``int``, *optional*):
            The intensity of the wallpaper.

        rotation (``int``, *optional*):
            The rotation of the wallpaper.

        emoticon (``str``, *optional*):
            The emoticon of the wallpaper.
    """

    def __init__(
        self,
        is_blur: bool = None,
        is_motion: bool = None,
        background_color: int = None,
        second_background_color: int = None,
        third_background_color: int = None,
        fourth_background_color: int = None,
        intensity: int = None,
        rotation: int = None,
        emoticon: str = None
    ):
        super().__init__()
        self.is_blur = is_blur
        self.is_motion = is_motion
        self.background_color = background_color
        self.second_background_color = second_background_color
        self.third_background_color = third_background_color
        self.fourth_background_color = fourth_background_color
        self.intensity = intensity
        self.rotation = rotation
        self.emoticon = emoticon

    @staticmethod
    def _parse(wallpaper_settings: "raw.types.WallPaperSettings") -> "WallpaperSettings":
        if wallpaper_settings is None:
            return None

        return WallpaperSettings(
            is_blur=getattr(wallpaper_settings, "blur", None),
            is_motion=getattr(wallpaper_settings, "motion", None),
            background_color=getattr(wallpaper_settings, "background_color", None),
            second_background_color=getattr(wallpaper_settings, "second_background_color", None),
            third_background_color=getattr(wallpaper_settings, "third_background_color", None),
            fourth_background_color=getattr(wallpaper_settings, "fourth_background_color", None),
            intensity=getattr(wallpaper_settings, "intensity", None),
            rotation=getattr(wallpaper_settings, "rotation", None),
            emoticon=getattr(wallpaper_settings, "emoticon", None)
        )
