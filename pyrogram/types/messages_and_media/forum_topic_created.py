from pyrogram import raw
from ..object import Object


class ForumTopicCreated(Object):
    """A service message about a new forum topic created in the chat.


    Parameters:
        id (``int``):
            Id of the topic.

        title (``str``):
            Name of the topic.

        icon_color (``int``):
            Color of the topic icon in decimal format.

        custom_emoji_id (``str``, *optional*):
            Unique identifier of the custom emoji shown as the topic icon.
    """

    def __init__(
        self, *,
        id: int,
        title: str,
        icon_color: int,
        custom_emoji_id: str = None
    ):
        super().__init__()

        self.id = id
        self.title = title
        self.icon_color = icon_color
        self.custom_emoji_id = custom_emoji_id

    @staticmethod
    def _parse(message: "raw.base.Message") -> "ForumTopicCreated":
        custom_emoji_id = getattr(message.action, "icon_emoji_id", None)

        return ForumTopicCreated(
            id=getattr(message, "id", None),
            title=getattr(message.action, "title", None),
            icon_color=getattr(message.action, "icon_color", None),
            custom_emoji_id=str(custom_emoji_id) if custom_emoji_id else None
        )
