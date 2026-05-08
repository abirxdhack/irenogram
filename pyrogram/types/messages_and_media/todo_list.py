
from typing import List, Dict

import pyrogram
from pyrogram import raw, types
from ..object import Object

class TodoList(Object):
    """A list of tasks.


    Parameters:
        title (``str``):
            Title of the todo list.

        entities (List of :obj:`~pyrogram.types.MessageEntity`):
            Entities in the title of the todo list.

        tasks (List of :obj:`~pyrogram.types.TodoTask`):
            List of tasks in the todo list.

        can_append (``bool``, optional):
            True, if other users can append tasks to this todo list.

        can_complete (``bool``, optional):
            True, if other users can complete tasks in this todo list.
    """

    def __init__(
        self,
        title: str,
        entities: List["types.MessageEntity"],
        tasks: List["types.TodoTask"] = None,
        can_append: bool = False,
        can_complete: bool = False
    ):
        super().__init__()

        self.title = title
        self.entities = entities
        self.tasks = tasks
        self.can_append = can_append
        self.can_complete = can_complete

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        todo: "raw.types.TodoList",
        users: Dict
    ) -> "TodoList":
        todo_list = todo.todo
        completions = todo.completions
        entities = [types.MessageEntity._parse(client, entity, None) for entity in todo_list.title.entities]
        entities = types.List(filter(lambda x: x is not None, entities))
        tasks = [
            types.TodoTask._parse(client, task, users, completions)
            for task in todo_list.list
        ] if todo_list.list else []
        return TodoList(
            title=todo_list.title.text,
            entities=entities,
            tasks=tasks,
            can_append=todo_list.others_can_append,
            can_complete=todo_list.others_can_complete
        )
