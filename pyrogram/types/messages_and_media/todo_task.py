
from typing import List, Dict

import pyrogram
from pyrogram import raw, types, utils
from ..object import Object

class TodoTask(Object):
    """A task in a todo list.


    Parameters:
        title (``str``):
            Title of the task.

        entities (List of :obj:`~pyrogram.types.MessageEntity`):
            Entities in the title of the task.

        is_completed (``bool``):
            True, if the task is completed.

        completed_by (:obj:`~pyrogram.types.User`, *optional*):
            User who completed the task.

        complete_date (:obj:`~datetime.datetime`, *optional*):
            Date when the task was completed.
    """

    def __init__(
        self,
        id: int,
        title: str,
        entities: List["types.MessageEntity"],
        is_completed: bool,
        completed_by: "types.User" = None,
        complete_date: "pyrogram.types.datetime" = None
    ):
        super().__init__()

        self.id = id
        self.title = title
        self.entities = entities
        self.is_completed = is_completed
        self.completed_by = completed_by
        self.complete_date = complete_date

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        todo_task: "raw.types.TodoTask",
        users: Dict,
        completions: List["raw.types.TodoTaskCompletion"] = None
    ) -> "TodoTask":
        entities = [types.MessageEntity._parse(client, entity, None) for entity in todo_task.title.entities]
        entities = types.List(filter(lambda x: x is not None, entities))
        complete = {i.id: i for i in completions} if completions else {}
        todo_completion = complete.get(todo_task.id)
        completed_by = types.User._parse(client, users.get(todo_completion.completed_by, None)) if todo_completion else None
        complete_date = utils.timestamp_to_datetime(todo_completion.date) if todo_completion else None
        return TodoTask(
            id=todo_task.id,
            title=todo_task.title.text,
            entities=entities,
            is_completed=True if todo_completion else False,
            completed_by=completed_by,
            complete_date=complete_date
        )
