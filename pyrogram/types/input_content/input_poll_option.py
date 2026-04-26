
from typing import Union

import pyrogram
from pyrogram import raw, types

from ..object import Object


class InputPollOption(Object):
    """This object contains information about one answer option in a poll to be sent.

    Parameters:
        text (``str`` | :obj:`~pyrogram.enums.FormattedText`, *optional*):
            Option text, 1-100 characters.
    """

    def __init__(
        self,
        *,
        text: Union[str, "types.FormattedText"],
    ):
        super().__init__()

        self.text = text

    async def write(self, client: "pyrogram.Client") -> "raw.types.InputPollAnswer":
        if isinstance(self.text, str):
            self.text = types.FormattedText(text=self.text)

        return raw.types.InputPollAnswer(
            text=await self.text.write(client)
        )
