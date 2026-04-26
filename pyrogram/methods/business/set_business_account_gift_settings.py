
import pyrogram
from pyrogram import raw

class SetBusinessAccountGiftSettings:
    async def set_business_account_gift_settings(
        self: "pyrogram.Client",
        business_connection_id: str,
        show_gift_button: bool = None,
        allow_unlimited_gifts: bool = True,
        allow_limited_gifts: bool = True,
        allow_unique_gifts: bool = True,
        allow_premium_gifts: bool = True
    ) -> bool:
        """Changes the privacy settings pertaining to incoming gifts for a managed business account.


        Parameters:
            business_connection_id (``str``): Unique identifier of the business connection.
            show_gift_button (``bool``, *optional*): Pass True to show the gift button in the profile.
            allow_unlimited_gifts (``bool``): Allow unlimited star gifts. Default True.
            allow_limited_gifts (``bool``): Allow limited star gifts. Default True.
            allow_unique_gifts (``bool``): Allow unique star gifts. Default True.
            allow_premium_gifts (``bool``): Allow premium gifts. Default True.

        Returns:
            ``bool``: True on success.
        """
        disallowed = raw.types.DisallowedGiftsSettings(
            disallow_unlimited_stargifts=not allow_unlimited_gifts or None,
            disallow_limited_stargifts=not allow_limited_gifts or None,
            disallow_unique_stargifts=not allow_unique_gifts or None,
            disallow_premium_gifts=not allow_premium_gifts or None,
        )

        r = await self.invoke(
            raw.functions.InvokeWithBusinessConnection(
                connection_id=business_connection_id,
                query=raw.functions.account.SetGlobalPrivacySettings(
                    settings=raw.types.GlobalPrivacySettings(
                        display_gifts_button=show_gift_button,
                        disallowed_gifts=disallowed
                    )
                )
            )
        )
        return bool(r)
