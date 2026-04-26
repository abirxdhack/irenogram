
import pyrogram
from pyrogram import raw

class SetBusinessAccountBio:
    async def set_business_account_bio(
        self: "pyrogram.Client",
        business_connection_id: str,
        bio: str = ""
    ) -> bool:
        """Changes the bio of a managed business account.


        Parameters:
            business_connection_id (``str``): Unique identifier of the business connection.
            bio (``str``): New bio; 0-70 characters.

        Returns:
            ``bool``: True on success.
        """
        r = await self.invoke(
            raw.functions.InvokeWithBusinessConnection(
                connection_id=business_connection_id,
                query=raw.functions.account.UpdateProfile(about=bio)
            )
        )
        return bool(r)
