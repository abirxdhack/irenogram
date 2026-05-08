
import pyrogram
from pyrogram import raw


class SetUpgradedGiftColors:
    async def set_upgraded_gift_colors(
        self: "pyrogram.Client",
        upgraded_gift_colors_id: int
    ) -> bool:
        """Changes color scheme for the current user based on an owned or a hosted upgraded gift.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            upgraded_gift_colors_id (``int``):
                Identifier of the color scheme to use.

        Returns:
            ``bool``: On success, True is returned.
        """
        r = await self.invoke(
            raw.functions.account.UpdateColor(
                color=raw.types.InputPeerColorCollectible(
                    collectible_id=upgraded_gift_colors_id
                )
            )
        )

        return r
