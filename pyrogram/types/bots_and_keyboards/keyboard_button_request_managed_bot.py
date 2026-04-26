
from ..object import Object


class KeyboardButtonRequestManagedBot(Object):
    """This object defines the parameters for the creation of a managed bot.

    Parameters:
        button_id (``int``):
            Identifier of button.

        suggested_name (``str``):
            Suggested name for the bot.

        suggested_username (``str``):
            Suggested username for the bot.
    """

    def __init__(
        self, *,
        button_id: int,
        suggested_name: str,
        suggested_username: str
    ):
        super().__init__()

        self.button_id = button_id
        self.suggested_name = suggested_name
        self.suggested_username = suggested_username
