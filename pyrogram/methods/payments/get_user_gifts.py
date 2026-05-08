
from typing import Union, Optional
import pyrogram
from pyrogram import raw, types

class GetUserGifts:
    async def get_user_gifts(
        self: "pyrogram.Client",
        user_id: Union[int, str],
        exclude_unsaved: Optional[bool] = None,
        exclude_saved: Optional[bool] = None,
        exclude_unlimited: Optional[bool] = None,
        exclude_limited: Optional[bool] = None,
        exclude_unique: Optional[bool] = None,
        sort_by_value: Optional[bool] = None,
        offset: str = "",
        limit: int = 0
    ):
        """Returns the gifts received by the given user or chat.


        Parameters:
            user_id (``int`` | ``str``): Target user.
            exclude_unsaved (``bool``, *optional*): Exclude gifts not saved to profile.
            exclude_saved (``bool``, *optional*): Exclude gifts saved to profile.
            exclude_unlimited (``bool``, *optional*): Exclude unlimited gifts.
            exclude_limited (``bool``, *optional*): Exclude limited gifts.
            exclude_unique (``bool``, *optional*): Exclude unique gifts.
            sort_by_value (``bool``, *optional*): Sort by value instead of date.
            offset (``str``, *optional*): Pagination offset.
            limit (``int``, *optional*): Max number to return.

        Returns:
            ``Generator``: Yields :obj:`~pyrogram.types.Gift` objects.
        """
        peer = await self.resolve_peer(user_id)
        current = 0
        total = abs(limit) or (1 << 31) - 1
        fetch_limit = min(100, total)

        while True:
            r = await self.invoke(
                raw.functions.payments.GetSavedStarGifts(
                    peer=peer,
                    offset=offset,
                    limit=fetch_limit,
                    exclude_unsaved=exclude_unsaved,
                    exclude_saved=exclude_saved,
                    exclude_unlimited=exclude_unlimited,
                    exclude_limited=exclude_limited,
                    exclude_unique=exclude_unique,
                    sort_by_value=sort_by_value
                )
            )

            users = {i.id: i for i in r.users}
            chats = {i.id: i for i in r.chats}

            gifts = [
                await types.Gift._parse_saved(self, gift, users, chats)
                for gift in r.gifts
            ]

            if not gifts:
                return

            for gift in gifts:
                yield gift
                current += 1
                if current >= total:
                    return

            offset = r.next_offset
            if not offset:
                return
