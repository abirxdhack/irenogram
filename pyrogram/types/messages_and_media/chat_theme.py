
from ..object import Object
from pyrogram import raw

class ChatTheme(Object):
    """A service message about a chat theme.

    parameters:
        emoticon (``str``):
            The emoticon of the chat theme.
    """

    def __init__(self, emoticon: str):
        super().__init__()
        self.emoticon = emoticon

    @staticmethod
    def _parse(chat_theme: "raw.types.MessageActionSetChatTheme") -> "ChatTheme":
        return ChatTheme(
            emoticon=getattr(chat_theme, "emoticon", None)
        )
