
from ..object import Object

class WebAppInfo(Object):
    """Contains information about a Web App.

    Parameters:
        url (``str``):
            An HTTPS URL of a Web App to be opened with additional data.
    """

    def __init__(
        self, *,
        url: str,
    ):
        super().__init__()

        self.url = url
