
from pyrogram import raw
from ..object import Object

class ForumTopicDeleted(Object):
    """A deleted forum topic.


    Parameters:
        id (``Integer``):
            Id of the topic
    """

    def __init__(
        self,
        *,
        id: int
    ):
        super().__init__()

        self.id = id

    @staticmethod
    def _parse(forum_topic: "raw.types.ForumTopicDeleted") -> "ForumTopicDeleted":
        return ForumTopicDeleted(
            id=getattr(forum_topic,"id", None)
        )
