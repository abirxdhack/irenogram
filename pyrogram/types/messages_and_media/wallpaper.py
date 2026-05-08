
import pyrogram

from ..object import Object
from pyrogram import raw, types

class Wallpaper(Object):
    """A wallpaper.

    parameters:
        id (``int``):
            Unique identifier for this wallpaper.

        slug (``str``):
            The slug of the wallpaper.

        document (:obj:`~pyrogram.types.Document`):
            The document of the wallpaper.

        is_creator (:obj:`bool`, optional):
            True, if the wallpaper was created by the current user.

        is_default (:obj:`bool`, optional):
            True, if the wallpaper is the default wallpaper.

        is_pattern (:obj:`bool`, optional):
            True, if the wallpaper is a pattern.

        id_dark (:obj:`bool`, optional):
            True, if the wallpaper is dark.

        settings (:obj:`~pyrogram.types.WallpaperSettings`, optional):
            The settings of the wallpaper.
    """

    def __init__(
        self,
        id: int,
        slug: str,
        document: "types.Document" = None,
        is_creator: bool = None,
        is_default: bool = None,
        is_pattern: bool = None,
        is_dark: bool = None,
        settings: "types.WallpaperSettings" = None
    ):
        super().__init__()
        self.id = id
        self.slug = slug
        self.document = document
        self.is_creator = is_creator
        self.is_default = is_default
        self.is_pattern = is_pattern
        self.is_dark = is_dark
        self.settings = settings

    @staticmethod
    def _parse(client: "pyrogram.Client", wallpaper: "raw.base.WallPaper") -> "Wallpaper":
        doc = None
        if not isinstance(wallpaper, raw.types.WallPaperNoFile):
            doc = wallpaper.document
        attributes = {type(i): i for i in doc.attributes}

        file_name = getattr(
            attributes.get(
                raw.types.DocumentAttributeFilename, None
            ), "file_name", None
        )
        return Wallpaper(
            id=wallpaper.id,
            slug=wallpaper.slug,
            document=types.Document._parse(client, doc, file_name) if doc is not None else None,
            is_creator=getattr(wallpaper, "creator", None),
            is_default=getattr(wallpaper, "default", None),
            is_pattern=getattr(wallpaper, "pattern", None),
            is_dark=getattr(wallpaper, "dark", None),
            settings=types.WallpaperSettings._parse(wallpaper.settings)
        )
