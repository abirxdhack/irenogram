
from typing import List, Optional

import pyrogram
from pyrogram import enums, raw, types, utils

from ..object import Object


class InputChecklistTask(Object):
    """Describes a task in a checklist to be sent.

    Parameters:
        id (``int``):
            Unique identifier of the task.

        text (``str``):
            Text of the task.

        parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
            The parse mode to use for the checklist.

        entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
            List of special entities that appear in the checklist title.
    """

    def __init__(
        self,
        *,
        id: int,
        text: str,
        parse_mode: Optional["enums.ParseMode"] = None,
        entities: Optional[List["types.MessageEntity"]] = None,
    ):
        super().__init__()

        self.id = id
        self.text = text
        self.parse_mode = parse_mode
        self.entities = entities

    async def write(
        self, client: "pyrogram.Client"
    ) -> "raw.types.TodoItem":
        task_title, task_entities = (await utils.parse_text_entities(
            client, self.text, self.parse_mode, self.entities
        )).values()

        return raw.types.TodoItem(
            id=self.id,
            title=raw.types.TextWithEntities(
                text=task_title,
                entities=task_entities or []
            )
        )
