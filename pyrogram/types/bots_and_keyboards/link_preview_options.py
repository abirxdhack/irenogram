
from typing import Optional

from ..object import Object

class LinkPreviewOptions(Object):
    """Options for link preview generation in a message (Bot API style).

    Use this with :meth:`~pyrogram.Client.send_message` as the
    ``link_preview_options`` parameter.  It maps to the underlying MTProto
    fields as follows:

    - ``is_disabled`` → ``no_webpage=True`` on ``messages.SendMessage``
    - ``url`` → ``url`` field on ``inputMediaWebPage``
    - ``prefer_large_media`` → ``force_large_media=True`` on ``inputMediaWebPage``
    - ``prefer_small_media`` → ``force_small_media=True`` on ``inputMediaWebPage``
    - ``show_above_text`` → ``invert_media=True`` on ``messages.SendMessage`` /
      ``messages.SendMedia``

    Parameters:
        is_disabled (``bool``, *optional*):
            ``True`` to disable link preview entirely.
            Equivalent to the legacy ``disable_web_page_preview=True`` parameter.

        url (``str``, *optional*):
            Specific URL to use for the preview.  Telegram will generate the
            preview from this URL instead of the first URL found in the text.

        prefer_large_media (``bool``, *optional*):
            ``True`` to force a large preview image.  Mutually exclusive with
            ``prefer_small_media``.

        prefer_small_media (``bool``, *optional*):
            ``True`` to force a small preview image.  Mutually exclusive with
            ``prefer_large_media``.

        show_above_text (``bool``, *optional*):
            ``True`` to place the link preview *above* the message text instead
            of below it.

    Example:
        .. code-block:: python

            from pyrogram.types import LinkPreviewOptions


            await app.send_message(
                "me", "https://pyrogram.org",
                link_preview_options=LinkPreviewOptions(is_disabled=True)
            )


            await app.send_message(
                "me", "Check this out: https://pyrogram.org",
                link_preview_options=LinkPreviewOptions(
                    prefer_large_media=True,
                    show_above_text=True
                )
            )


            await app.send_message(
                "me", "Click here",
                link_preview_options=LinkPreviewOptions(url="https://pyrogram.org")
            )
    """

    def __init__(
        self,
        *,
        is_disabled: Optional[bool] = None,
        url: Optional[str] = None,
        prefer_large_media: Optional[bool] = None,
        prefer_small_media: Optional[bool] = None,
        show_above_text: Optional[bool] = None,
    ):
        super().__init__()
        self.is_disabled = is_disabled
        self.url = url
        self.prefer_large_media = prefer_large_media
        self.prefer_small_media = prefer_small_media
        self.show_above_text = show_above_text
