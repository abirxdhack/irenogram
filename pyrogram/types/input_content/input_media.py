from typing import TYPE_CHECKING, BinaryIO, List, Optional, Union

from ..messages_and_media import MessageEntity
from ..object import Object

if TYPE_CHECKING:
    from pyrogram import raw


class InputMedia(Object):
    """Content of a media message to be sent.

    It should be one of:

    - :obj:`~pyrogram.types.InputMediaAnimation`
    - :obj:`~pyrogram.types.InputMediaDocument`
    - :obj:`~pyrogram.types.InputMediaAudio`
    - :obj:`~pyrogram.types.InputMediaPhoto`
    - :obj:`~pyrogram.types.InputMediaVideo`
    - :obj:`~pyrogram.types.InputMediaSticker`
    """

    def __init__(
        self,
        media: Union[str, BinaryIO],
        caption: str = "",
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
    ):
        super().__init__()

        self.media = media
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities

    async def write(self, **kwargs) -> "raw.base.InputMedia":
        raise NotImplementedError