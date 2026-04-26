from typing import Union

import pyrogram
from pyrogram import raw, types


class FixTextWithAI:
    async def fix_text_with_ai(
        self: "pyrogram.Client",
        text: Union[str, "types.FormattedText"],
    ) -> "types.FormattedText":
        """Fixes text using an AI model.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            text (``str`` | :obj:`~pyrogram.types.FormattedText`):
                The original text.

        Returns:
            :obj:`~pyrogram.types.FormattedText`: On success, information about the fixed text is returned.
        """
        if isinstance(text, str):
            text = types.FormattedText(text=text)

        r = await self.invoke(
            raw.functions.messages.ComposeMessageWithAI(
                text=await text.write(self),
                proofread=True,
            )
        )

        return types.FormattedText._parse(self, r.result_text)
