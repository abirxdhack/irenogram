
from typing import List

from pyrogram import raw
from ..object import Object

class TodoTasksIncompleted(Object):
    """One or more todo task/s has been flag as incomplete.


    Parameters:
        ids (List of ``int``):
            List of Unique identifier of the todo tasks.
    """

    def __init__(self, ids: List[int]):
        super().__init__()

        self.ids = ids

    @staticmethod
    def _parse(todo_completion: "raw.types.TodoCompletion") -> "TodoTasksIncompleted":
        ids = [id for id in todo_completion.incompleted]
        return TodoTasksIncompleted(
            ids=ids,
        )
