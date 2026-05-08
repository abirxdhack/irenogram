
from datetime import datetime
from typing import Dict, List, Optional

import pyrogram
from pyrogram import raw, types, utils

from ..object import Object


class Checklist(Object):
    """Describes a checklist.

    Parameters:
        title (``str``):
            Title of the checklist.

        entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
            Entities in the title of the checklist.
            May contain only Bold, Italic, Underline, Strikethrough, Spoiler, and CustomEmoji entities.

        tasks (List of :obj:`~pyrogram.types.ChecklistTask`, *optional*):
            List of tasks in the checklist.

        others_can_add_tasks (``bool``, *optional*):
            True, if users other than creator of the list can add tasks to the list.

        can_add_tasks (``bool``, *optional*):
            True, if the current user can add tasks to the list if they have Telegram Premium subscription.

        others_can_mark_tasks_as_done (``bool``, *optional*):
            True, if users other than creator of the list can mark tasks as done or not done.
            If True, then the checklist is called "group checklist".

        can_mark_tasks_as_done (``bool``, *optional*):
            True, if the current user can mark tasks as done or not done if they have Telegram Premium subscription.
    """

    def __init__(
        self,
        *,
        title: str,
        entities: Optional[List["types.MessageEntity"]] = None,
        tasks: Optional[List["types.ChecklistTask"]] = None,
        others_can_add_tasks: Optional[bool] = None,
        can_add_tasks: Optional[bool] = None,
        others_can_mark_tasks_as_done: Optional[bool] = None,
        can_mark_tasks_as_done: Optional[bool] = None,
    ):
        super().__init__()

        self.title = title
        self.entities = entities
        self.tasks = tasks
        self.others_can_add_tasks = others_can_add_tasks
        self.can_add_tasks = can_add_tasks
        self.others_can_mark_tasks_as_done = others_can_mark_tasks_as_done
        self.can_mark_tasks_as_done = can_mark_tasks_as_done

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        checklist: "raw.types.MessageMediaToDo",
        users: Dict[int, "raw.base.User"],
        chats: Dict[int, "raw.base.Chat"],
    ) -> "Checklist":
        completions = {i.id: i for i in getattr(checklist, "completions", [])}

        checklist_tasks = []

        for task in checklist.todo.list:
            checklist_tasks.append(
                types.ChecklistTask._parse(
                    client,
                    task,
                    completions.get(task.id),
                    users,
                    chats
                )
            )

        title, entities = (
            utils.parse_text_with_entities(client, checklist.todo.title, users)
        ).values()

        return Checklist(
            title=title,
            entities=entities,
            tasks=checklist_tasks,
            others_can_add_tasks=checklist.todo.others_can_append,
            others_can_mark_tasks_as_done=checklist.todo.others_can_complete,
        )
