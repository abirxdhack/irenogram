
from pyrogram import raw

from ..object import Object


class PaymentOption(Object):
    """Describes an additional payment option.

    Parameters:
        title (``str``):
            Title for the payment option.

        url (``str``):
            Payment form URL to be opened in a web view.
    """
    def __init__(
        self,
        *,
        title: str,
        url: str
    ):
        super().__init__()

        self.title = title
        self.url = url

    @staticmethod
    def _parse(option: "raw.base.PaymentFormMethod") -> "PaymentOption":
        return PaymentOption(
            title=option.title,
            url=option.url
        )
