
from typing import Optional

from pyrogram import raw

from ..object import Object


class LinkPreviewOptions(Object):
    """Describes the options used for link preview generation.

    Parameters:
        is_disabled (``bool``, *optional*):
            True, if the link preview is disabled.

        url (``str``, *optional*):
            URL to use for the link preview.
            If empty, then the first URL found in the message text will be used.

        prefer_small_media (``bool``, *optional*):
            True, if the media in the link preview is suppposed to be shrunk.
            Ignored if the URL isn't explicitly specified or media size change isn't supported for the preview.

        prefer_large_media (``bool``, *optional*):
            True, if the media in the link preview is suppposed to be enlarged.
            Ignored if the URL isn't explicitly specified or media size change isn't supported for the preview.

        show_above_text (``bool``, *optional*):
            True, if the link preview must be shown above the message text.
            Otherwise, the link preview will be shown below the message text.
    """

    def __init__(
        self,
        *,
        is_disabled: bool = None,
        url: str = None,
        prefer_small_media: bool = None,
        prefer_large_media: bool = None,
        show_above_text: bool = None
    ):
        super().__init__()

        self.is_disabled = is_disabled
        self.url = url
        self.prefer_small_media = prefer_small_media
        self.prefer_large_media = prefer_large_media
        self.show_above_text = show_above_text

    @staticmethod
    def _parse(
        media: "raw.types.MessageMediaWebPage",
        url: str = None,
        invert_media: bool = None
    ) -> Optional["LinkPreviewOptions"]:
        if isinstance(media, raw.types.MessageMediaWebPage) and not isinstance(media.webpage, raw.types.WebPageNotModified):
            return LinkPreviewOptions(
                is_disabled=False,
                url=media.webpage.url,
                prefer_small_media=media.force_small_media,
                prefer_large_media=media.force_large_media,
                show_above_text=invert_media,
            )

        if url:
            return LinkPreviewOptions(
                is_disabled=True,
                url=url,
                show_above_text=invert_media,
            )
