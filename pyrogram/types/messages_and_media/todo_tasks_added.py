
import pyrogram

from pyrogram import raw, types
from ..object import Object

class TodoTasksAdded(Object):
    """A todo task added to a todo list.


    Parameters:
        task (:obj:`~pyrogram.types.TodoTask`):
            The added todo task.
    """

    def __init__(self, tasks: "types.TodoTask"):
        super().__init__()

        self.tasks = tasks

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        todo_task_added: "raw.types.MessageActionTodoAppendTasks"
    ) -> "TodoTasksAdded":
        return TodoTasksAdded(
            tasks=[types.TodoTask._parse(client, task, {}, {}) for task in todo_task_added.list]
        )
