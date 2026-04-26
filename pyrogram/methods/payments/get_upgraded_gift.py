
import pyrogram
from pyrogram import raw, types


class GetUpgradedGift:
    async def get_upgraded_gift(
        self: "pyrogram.Client",
        link: str
    ) -> "types.Gift":
        """Get information about upgraded gift.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            link (``str``):
                The gift code link or slug itself.

        Returns:
            :obj:`~pyrogram.types.Gift`: Information about the gift is returned.

        Example:
            .. code-block:: python

                gift = await client.get_upgraded_gift("https://t.me/nft/SignetRing-903")

                gift = await client.get_upgraded_gift("SignetRing-903")
        """
        match = self.UPGRADED_GIFT_RE.match(link)

        if match:
            slug = match.group(1)
        elif isinstance(link, str):
            slug = link
        else:
            raise ValueError("Invalid gift link")

        r = await self.invoke(
            raw.functions.payments.GetUniqueStarGift(
                slug=slug.replace(" ", "")
            )
        )

        users = {i.id: i for i in r.users}
        chats = {i.id: i for i in r.chats}

        return await types.Gift._parse(self, r.gift, users=users, chats=chats)
