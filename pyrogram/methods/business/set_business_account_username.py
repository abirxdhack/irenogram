
import pyrogram
from pyrogram import raw

class SetBusinessAccountUsername:
    async def set_business_account_username(
        self: "pyrogram.Client",
        business_connection_id: str,
        username: str = ""
    ) -> bool:
        """Changes the username of a managed business account.


        Parameters:
            business_connection_id (``str``): Unique identifier of the business connection.
            username (``str``): New username. Pass empty string to remove.

        Returns:
            ``bool``: True on success.
        """
        r = await self.invoke(
            raw.functions.InvokeWithBusinessConnection(
                connection_id=business_connection_id,
                query=raw.functions.account.UpdateUsername(username=username)
            )
        )
        return bool(r)
