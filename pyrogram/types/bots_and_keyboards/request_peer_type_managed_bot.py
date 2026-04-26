
from typing import Optional
from ..object import Object

class RequestPeerTypeManagedBot(Object):
    """Criteria for requesting a managed bot creation via a keyboard button.


    Parameters:
        button_id (``int``, *optional*):
            Button identifier. Defaults to 0.

        bot_managed (``bool``, *optional*):
            If True, the created bot will be set as managed by the requesting bot.

        suggested_name (``str``, *optional*):
            Pre-filled name suggestion shown to the user during bot creation.

        suggested_username (``str``, *optional*):
            Pre-filled username suggestion shown to the user during bot creation.
    """

    def __init__(
        self,
        button_id: int = 0,
        bot_managed: Optional[bool] = None,
        suggested_name: Optional[str] = None,
        suggested_username: Optional[str] = None,
    ):
        super().__init__()

        self.button_id = button_id
        self.bot_managed = bot_managed
        self.suggested_name = suggested_name
        self.suggested_username = suggested_username
