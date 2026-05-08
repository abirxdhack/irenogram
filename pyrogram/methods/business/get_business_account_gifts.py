
from typing import Optional, AsyncGenerator

import pyrogram
from pyrogram import raw, types
from pyrogram import utils


class GetBusinessAccountGifts:
    async def get_business_account_gifts(
        self: "pyrogram.Client",
        business_connection_id: str,
        collection_id: Optional[int] = None,
        exclude_unsaved: Optional[bool] = None,
        exclude_saved: Optional[bool] = None,
        exclude_unlimited: Optional[bool] = None,
        exclude_upgradable: Optional[bool] = None,
        exclude_non_upgradable: Optional[bool] = None,
        exclude_upgraded: Optional[bool] = None,
        exclude_without_colors: Optional[bool] = None,
        exclude_hosted: Optional[bool] = None,
        sort_by_price: Optional[bool] = None,
        limit: int = 0,
        offset: str = "",
    ) -> AsyncGenerator["types.Gift", None]:
        """Return the gifts received and owned by a managed business account.

        .. note::

            Requires the `can_view_gifts_and_stars` business bot right.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            business_connection_id (``str``):
                Unique identifier of business connection on behalf of which to send the request.

            collection_id (``int``, *optional*):
                Pass collection identifier to get gifts only from the specified collection.

            exclude_unsaved (``bool``, *optional*):
                Pass True to exclude gifts that aren't saved to the account's profile page.

            exclude_saved (``bool``, *optional*):
                Pass True to exclude gifts that are saved to the account's profile page.

            exclude_unlimited (``bool``, *optional*):
                Pass True to exclude gifts that can be purchased an unlimited number of times.

            exclude_upgradable (``bool``, *optional*):
                Pass True to exclude gifts that can be purchased limited number of times and can be upgraded.

            exclude_non_upgradable (``bool``, *optional*):
                Pass True to exclude gifts that can be purchased limited number of times and can't be upgraded.

            exclude_upgraded (``bool``, *optional*):
                Pass True to exclude upgraded gifts.

            exclude_without_colors (``bool``, *optional*):
                Pass True to exclude gifts that can't be used in set_upgraded_gift_colors.

            exclude_hosted (``bool``, *optional*):
                Pass True to exclude gifts that are just hosted and are not owned by the owner.

            sort_by_price (``bool``, *optional*):
                Pass True to sort results by gift price instead of send date. Sorting is applied before pagination.

            limit (``int``, *optional*):
                The maximum number of gifts to be returned.

            offset (``str``, *optional*):
                Offset of the first entry to return as received from the previous request.

        Returns:
            ``Generator``: A generator yielding :obj:`~pyrogram.types.Gift` objects.

        Example:
            .. code-block:: python

                async for gift in app.get_business_account_gifts(connection_id):
                    print(gift)
        """
        current = 0
        total = abs(limit) or (1 << 31) - 1
        limit = min(100, total)

        connection_info = await self.get_business_connection(business_connection_id)

        peer = await self.resolve_peer(connection_info.user.id)
        raw_peer_id = utils.get_raw_peer_id(peer)

        while True:
            r = await self.invoke(
                raw.functions.payments.GetSavedStarGifts(
                    peer=peer,
                    offset=offset,
                    limit=limit,
                    exclude_unsaved=exclude_unsaved,
                    exclude_saved=exclude_saved,
                    exclude_unlimited=exclude_unlimited,
                    exclude_upgradable=exclude_upgradable,
                    exclude_non_upgradable=exclude_non_upgradable,
                    exclude_unique=exclude_upgraded,
                    exclude_without_colors=exclude_without_colors,
                    exclude_hosted=exclude_hosted,
                    sort_by_value=sort_by_price
                ),
                sleep_threshold=60,
                business_connection_id=business_connection_id
            )

            users = {i.id: i for i in r.users}
            chats = {i.id: i for i in r.chats}

            user_star_gifts = [
                await types.Gift._parse_saved(self, gift, users, chats)
                for gift in r.gifts
            ]

            if not user_star_gifts:
                return

            for gift in user_star_gifts:
                yield gift

                current += 1

                if current >= total:
                    return

            offset = r.next_offset
