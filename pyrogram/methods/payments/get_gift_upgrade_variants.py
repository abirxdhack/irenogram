
import pyrogram
from pyrogram import raw, types


class GetGiftUpgradeVariants:
    async def get_gift_upgrade_variants(
        self: "pyrogram.Client",
        gift_id: int
    ) -> "types.GiftUpgradeVariants":
        """Returns all possible variants of upgraded gifts for a regular gift.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            gift_id (``int``):
                Identifier of the gift.

        Returns:
            :obj:`~pyrogram.types.GiftUpgradeVariants`: On success, returns all possible variants of upgraded gifts for the given regular gift.
        """
        r = await self.invoke(
            raw.functions.payments.GetStarGiftUpgradeAttributes(
                gift_id=gift_id
            )
        )

        return await types.GiftUpgradeVariants._parse(self, r)
