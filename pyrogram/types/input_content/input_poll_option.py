from typing import Optional, Union

import pyrogram
from pyrogram import raw, types

from ..object import Object


class InputPollOption(Object):
    """This object contains information about one answer option in a poll to be sent.

    Parameters:
        text (``str`` | :obj:`~pyrogram.types.FormattedText`):
            Option text, 1-100 characters.

        media (:obj:`~pyrogram.types.InputMediaPhoto` | :obj:`~pyrogram.types.InputMediaVideo` | :obj:`~pyrogram.types.InputMediaSticker` | :obj:`~pyrogram.types.Location`, *optional*):
            Option media.
            Currently, can be only of the types Photo, Video, Sticker or Location.
    """

    def __init__(
        self,
        *,
        text: Union[str, "types.FormattedText"],
        media: Optional[Union[
            "types.InputMediaPhoto",
            "types.InputMediaVideo",
            "types.InputMediaSticker",
            "types.Location",
        ]] = None,
    ):
        super().__init__()

        self.text = text
        self.media = media

    async def write(self, client: "pyrogram.Client") -> "raw.types.InputPollAnswer":
        if isinstance(self.text, str):
            self.text = types.FormattedText(text=self.text)

        raw_media = None
        if self.media is not None:
            raw_media = await self.media.write(client=client)

        return raw.types.InputPollAnswer(
            text=await self.text.write(client),
            media=raw_media
        )
