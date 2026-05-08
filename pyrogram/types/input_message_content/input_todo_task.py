
from ..object import Object

class InputTodoTask(Object):
    """Contains information about a todo task.


    Parameters:
        title (``str``):
            Title of the task.

        entities (List of :obj:`~pyrogram.types.MessageEntity`):
            Entities in the title of the task.
    """

    def __init__(self, *, title: str, entities: list = None):
        super().__init__()

        self.title = title
        self.entities = entities
