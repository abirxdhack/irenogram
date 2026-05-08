
from typing import Optional

import pyrogram
from pyrogram import raw

from ..object import Object


class PaymentResult(Object):
    """Contains the result of a payment request.

    Parameters:
        success (``bool``):
            True, if the payment request was successful.
            Otherwise, the verification_url will be non-empty.

        verification_url (``str``, *optional*):
            URL for additional payment credentials verification.

        raw (:obj:`~pyrogram.raw.base.payments.PaymentResult`, *optional*):
            The raw result from the Telegram API.
    """
    def __init__(
        self,
        *,
        success: bool,
        verification_url: Optional[str] = None,
        raw: "raw.base.payments.PaymentResult" = None,
    ):
        super().__init__()

        self.success = success
        self.verification_url = verification_url
        self.raw = raw

    @staticmethod
    def _parse(payment_result: "raw.base.payments.PaymentResult") -> "PaymentResult":
        if isinstance(payment_result, raw.types.payments.PaymentVerificationNeeded):
            return PaymentResult(
                success=False,
                verification_url=payment_result.url,
                raw=payment_result
            )
        elif isinstance(payment_result, raw.types.payments.PaymentResult):
            return PaymentResult(
                success=True,
                raw=payment_result
            )
