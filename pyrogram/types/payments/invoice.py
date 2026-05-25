
from pyrogram import raw
from ..object import Object

class Invoice(Object):
    """Contains information about an Invoice.


    Parameters:
        title (``str``):
            Product name.

        description (``str``):
            Product description.

        currency (``str``):
            Currency code.

        total_amount (``int``):
            Total price in the smallest units of the currency.

        start_parameter (``str``):
            Unique bot deep-linking parameter that can be used to generate this invoice.

        shipping_address_requested (``bool``, *optional*):
            True, if the the shipping address is requested.

        test (``bool``, *optional*):
            True, if the invoice is a test invoice.

        receipt_message_id (``int``, *optional*):
            The message_id of the message sent to the chat when the invoice is paid.
    """

    def __init__(
        self,
        *,
        title: str,
        description :  str,
        currency: str,
        total_amount: int,
        start_parameter: str,
        shipping_address_requested: bool = None,
        test: bool = None,
        receipt_message_id: int = None,

    ):
        super().__init__()

        self.title = title
        self.description = description
        self.currency = currency
        self.total_amount = total_amount
        self.start_parameter = start_parameter
        self.shipping_address_requested = shipping_address_requested
        self.test = test
        self.receipt_message_id = receipt_message_id

    @staticmethod
    def _parse(
        client=None,
        message_invoice: "raw.types.MessageMediaInvoice" = None,
    ) -> "Invoice":
        if message_invoice is None:
            return None
        return Invoice(
            title=message_invoice.title,
            description=message_invoice.description,
            currency=message_invoice.currency,
            total_amount=message_invoice.total_amount,
            start_parameter=getattr(message_invoice, "start_param", None),
            shipping_address_requested=getattr(message_invoice, "shipping_address_requested", None),
            test=getattr(message_invoice, "test", None),
            receipt_message_id=getattr(message_invoice, "receipt_msg_id", None),
        )
