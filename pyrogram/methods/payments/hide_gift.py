import pyrogram
from pyrogram import raw

class HideGift:
    async def hide_gift(
        self: "pyrogram.Client",
        message_id: int
    ) -> bool:
        """Hide the star gift from your profile.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            message_id (``int``):
                Unique message identifier of star gift.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                # Hide gift
                app.hide_gift(message_id=123)
        """
        r = await self.invoke(
            raw.functions.payments.SaveStarGift(
                stargift=raw.types.InputSavedStarGiftUser(
                    msg_id=message_id
                ),
                unsave=True
            )
        )

        return r
