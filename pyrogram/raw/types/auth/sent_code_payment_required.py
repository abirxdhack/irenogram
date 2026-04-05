#  Pyrofork - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#  Copyright (C) 2022-present Mayuri-Chan <https://github.com/Mayuri-Chan>
#
#  This file is part of Pyrofork.
#
#  Pyrofork is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrofork is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrofork.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class SentCodePaymentRequired(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.auth.SentCode`.

    Details:
        - Layer: ``224``
        - ID: ``E0955A3C``

    Parameters:
        store_product (``str``):
            N/A

        phone_code_hash (``str``):
            N/A

        support_email_address (``str``):
            N/A

        support_email_subject (``str``):
            N/A

        currency (``str``):
            N/A

        amount (``int`` ``64-bit``):
            N/A

    Functions:
        This object can be returned by 7 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.SendCode
            auth.ResendCode
            auth.ResetLoginEmail
            auth.CheckPaidAuth
            account.SendChangePhoneCode
            account.SendConfirmPhoneCode
            account.SendVerifyPhoneCode
    """

    __slots__: List[str] = ["store_product", "phone_code_hash", "support_email_address", "support_email_subject", "currency", "amount"]

    ID = 0xe0955a3c
    QUALNAME = "types.auth.SentCodePaymentRequired"

    def __init__(self, *, store_product: str, phone_code_hash: str, support_email_address: str, support_email_subject: str, currency: str, amount: int) -> None:
        self.store_product = store_product  # string
        self.phone_code_hash = phone_code_hash  # string
        self.support_email_address = support_email_address  # string
        self.support_email_subject = support_email_subject  # string
        self.currency = currency  # string
        self.amount = amount  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodePaymentRequired":
        # No flags
        
        store_product = String.read(b)
        
        phone_code_hash = String.read(b)
        
        support_email_address = String.read(b)
        
        support_email_subject = String.read(b)
        
        currency = String.read(b)
        
        amount = Long.read(b)
        
        return SentCodePaymentRequired(store_product=store_product, phone_code_hash=phone_code_hash, support_email_address=support_email_address, support_email_subject=support_email_subject, currency=currency, amount=amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.store_product))
        
        b.write(String(self.phone_code_hash))
        
        b.write(String(self.support_email_address))
        
        b.write(String(self.support_email_subject))
        
        b.write(String(self.currency))
        
        b.write(Long(self.amount))
        
        return b.getvalue()
