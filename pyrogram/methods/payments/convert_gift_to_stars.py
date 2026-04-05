import pyrogram
from pyrogram import raw

class ConvertGiftToStars:
    async def convert_gift_to_stars(
        self: "pyrogram.Client",
        message_id: int
    ) -> bool:
        """Convert a received star gift to Telegram Stars.

        Parameters:
            message_id (``int``): Message ID of the gift to convert.

        Returns:
            ``bool``: True on success.
        """
        return await self.invoke(
            raw.functions.payments.ConvertStarGift(
                stargift=raw.types.InputSavedStarGiftUser(msg_id=message_id)
            )
        )
