
from typing import List, Union

import pyrogram
from pyrogram import raw
from pyrogram import types
from ..object import Object

class InlineKeyboardMarkup(Object):
    """An inline keyboard that appears right next to the message it belongs to.


    Parameters:
        inline_keyboard (List of List of :obj:`~pyrogram.types.InlineKeyboardButton` | :obj:`~pyrogram.types.InlineKeyboardButtonBuy`):
            List of button rows, each represented by a List of InlineKeyboardButton objects.
            :obj:`~pyrogram.types.InlineKeyboardButtonBuy` objects is only for :meth:`~pyrogram.Client.send_invoice`.
            and only one needed in the first row.
    """

    def __init__(self, inline_keyboard: List[List[Union["types.InlineKeyboardButton", "types.InlineKeyboardButtonBuy"]]]):
        super().__init__()

        self.inline_keyboard = inline_keyboard

    @staticmethod
    def read(o):
        """Deserialize a raw Telegram TL byte buffer into this object."""
        inline_keyboard = []

        for i in o.rows:
            row = []

            for j in i.buttons:
                row.append(types.InlineKeyboardButton.read(j))

            inline_keyboard.append(row)

        return InlineKeyboardMarkup(
            inline_keyboard=inline_keyboard
        )

    async def write(self, client: "pyrogram.Client"):
        """Serialize this object into a raw Telegram TL representation."""
        rows = []

        for r in self.inline_keyboard:
            buttons = []

            for b in r:
                buttons.append(await b.write(client))

            rows.append(raw.types.KeyboardButtonRow(buttons=buttons))

        return raw.types.ReplyInlineMarkup(rows=rows)

