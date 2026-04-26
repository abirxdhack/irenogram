
import pyrogram
from pyrogram import raw

class ConvertGift:
    async def convert_gift(
        self: "pyrogram.Client",
        message_id: int
    ) -> bool:
        """Convert star gift to stars.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            message_id (``int``):
                Unique message identifier of star gift.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python


                app.convert_gift(message_id=123)
        """
        r = await self.invoke(
            raw.functions.payments.ConvertStarGift(
                stargift=raw.types.InputSavedStarGiftUser(msg_id=message_id)
            )
        )

        return r
