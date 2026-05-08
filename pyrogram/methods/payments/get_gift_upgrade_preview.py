import pyrogram
from pyrogram import raw, types


class GetGiftUpgradePreview:
    async def get_gift_upgrade_preview(
        self: "pyrogram.Client",
        gift_id: int
    ) -> "types.GiftUpgradePreview":
        """Return examples of possible upgraded gifts for a regular gift.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            gift_id (``int``):
                Identifier of the gift.

        Returns:
            :obj:`~pyrogram.types.GiftUpgradePreview`: Information about the gift preview is returned.

        Example:
            .. code-block:: python

                await client.get_gift_upgrade_preview(5936085638515261992)
        """
        r = await self.invoke(
            raw.functions.payments.GetStarGiftUpgradePreview(
                gift_id=gift_id
            )
        )

        return await types.GiftUpgradePreview._parse(self, r)
