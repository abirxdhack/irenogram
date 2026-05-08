
import pyrogram
from pyrogram import raw, types


class GetUpgradedGiftValueInfo:
    async def get_upgraded_gift_value_info(
        self: "pyrogram.Client",
        link: str
    ) -> "types.UpgradedGiftValueInfo":
        """Returns information about value of an upgraded gift by its name.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            link (``str``):
                The gift link or slug itself.

        Returns:
            :obj:`~pyrogram.types.UpgradedGiftValueInfo`: Information about the gift value is returned.

        Example:
            .. code-block:: python

                gift = await client.get_upgraded_gift_value_info("https://t.me/nft/SignetRing-903")

                gift = await client.get_upgraded_gift_value_info("SignetRing-903")
        """
        match = self.UPGRADED_GIFT_RE.match(link)

        if match:
            slug = match.group(1)
        elif isinstance(link, str):
            slug = link
        else:
            raise ValueError("Invalid gift link")

        r = await self.invoke(
            raw.functions.payments.GetUniqueStarGiftValueInfo(
                slug=slug.replace(" ", "")
            )
        )

        return types.UpgradedGiftValueInfo._parse(r)
