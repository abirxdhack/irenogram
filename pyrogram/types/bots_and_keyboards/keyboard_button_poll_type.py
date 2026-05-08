
from ..object import Object


class KeyboardButtonPollType(Object):
    """Contains information about a poll type.

    Parameters:
        is_quiz (``bool``):
            If True, the requested poll will be sent as quiz.
    """

    def __init__(
        self, *,
        is_quiz: bool = None
    ):
        super().__init__()

        self.is_quiz = is_quiz
