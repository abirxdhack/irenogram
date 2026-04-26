
from typing import Dict, List

import pyrogram
from pyrogram import raw, types

from ..object import Object


class ChecklistTasksAdded(Object):
    """Some tasks were added to a checklist.

    Parameters:
        checklist_message_id (``int``):
            Identifier of the message with the checklist.
            Can be None if the message was deleted.

        tasks (List of :obj:`~pyrogram.types.ChecklistTask`):
            List of tasks added to the checklist.
    """

    def __init__(
        self,
        *,
        checklist_message_id: int,
        tasks: List["types.ChecklistTask"]
    ):

        super().__init__()

        self.checklist_message_id = checklist_message_id
        self.tasks = tasks

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        message: "raw.types.MessageService",
        users: Dict[int, "raw.base.User"],
        chats: Dict[int, "raw.base.Chat"]
    ) -> "ChecklistTasksAdded":
        action: "raw.types.MessageActionTodoAppendTasks" = message.action

        return ChecklistTasksAdded(
            checklist_message_id=getattr(message.reply_to, "reply_to_msg_id", None),
            tasks=types.List([types.ChecklistTask._parse(client, task, None, users, chats) for task in action.list])
        )
