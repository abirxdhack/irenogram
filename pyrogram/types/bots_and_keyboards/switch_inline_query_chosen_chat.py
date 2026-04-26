
from ..object import Object

class SwitchInlineQueryChosenChat(Object):
    """Represents an inline button that switches the current user to inline mode in a chosen chat.


    Parameters:
        query (``str``, *optional*):
            The default inline query to be inserted in the input field. Defaults to empty string.

        allow_user_chats (``bool``, *optional*):
            True if private chats with users can be chosen.

        allow_bot_chats (``bool``, *optional*):
            True if private chats with bots can be chosen.

        allow_group_chats (``bool``, *optional*):
            True if group and supergroup chats can be chosen.

        allow_channel_chats (``bool``, *optional*):
            True if channel chats can be chosen.
    """

    def __init__(
        self,
        query: str = "",
        allow_user_chats: bool = None,
        allow_bot_chats: bool = None,
        allow_group_chats: bool = None,
        allow_channel_chats: bool = None
    ):
        super().__init__()
        self.query = query
        self.allow_user_chats = allow_user_chats
        self.allow_bot_chats = allow_bot_chats
        self.allow_group_chats = allow_group_chats
        self.allow_channel_chats = allow_channel_chats
