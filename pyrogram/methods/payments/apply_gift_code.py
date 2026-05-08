import re

import pyrogram
from pyrogram import raw


class ApplyGiftCode:
    async def apply_gift_code(
        self: "pyrogram.Client",
        link: str,
    ) -> bool:
        """Apply a gift code.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            link (``str``):
                The gift code link.

        Returns:
            ``bool``: On success, True is returned.

        Raises:
            :raises ValueError: In case the gift code link is invalid.

        Example:
            .. code-block:: python

                await app.apply_gift_code("t.me/giftcode/abc1234567def")
        """
        match = re.match(r"^(?:https?://)?(?:www\.)?(?:t(?:elegram)?\.(?:org|me|dog)/(?:giftcode/|\+))([\w-]+)$", link)

        if match:
            slug = match.group(1)
        elif isinstance(link, str):
            slug = link
        else:
            raise ValueError("Invalid gift code link")

        await self.invoke(
            raw.functions.payments.ApplyGiftCode(
                slug=slug
            )
        )

        return True
