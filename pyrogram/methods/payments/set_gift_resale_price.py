
import pyrogram
from pyrogram import raw, types, utils


class SetGiftResalePrice:
    async def set_gift_resale_price(
        self: "pyrogram.Client",
        owned_gift_id: str,
        price: "types.GiftResalePrice" = None,
    ) -> bool:
        """Change resale price of a unique gift owned by the current user.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            owned_gift_id (``str``):
                Unique identifier of the target gift.
                For a user gift, you can use the message ID (int) of the gift message.
                For a channel gift, you can use the packed format `chatID_savedID` (str).
                For a upgraded gift, you can use the gift link.

            price (:obj:`~pyrogram.types.GiftResalePrice`, *optional*):
                The new price for the unique gift.
                Pass None to disallow gift resale.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                await app.set_gift_resale_price(
                    owned_gift_id="123456",
                    price=types.GiftResalePriceStar(star_count=100)
                )

                await app.set_gift_resale_price(
                    owned_gift_id="123456",
                    price=types.GiftResalePriceTon(toncoin_cent_count=10000000000) # You can use utils.to_nano(10) for same result
                )

                await app.set_gift_resale_price(owned_gift_id="123456")
        """
        await self.invoke(
            raw.functions.payments.UpdateStarGiftPrice(
                stargift=await utils.get_input_stargift(self, owned_gift_id),
                resell_amount=raw.types.StarsAmount(amount=0, nanos=0) if price is None else price.write()
            )
        )

        return True
