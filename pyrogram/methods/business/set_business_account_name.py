
import pyrogram
from pyrogram import raw

class SetBusinessAccountName:
    async def set_business_account_name(
        self: "pyrogram.Client",
        business_connection_id: str,
        first_name: str,
        last_name: str = ""
    ) -> bool:
        """Changes the first and last name of a managed business account.


        Parameters:
            business_connection_id (``str``):
                Unique identifier of the business connection.

            first_name (``str``):
                New value of the first name; 1-64 characters.

            last_name (``str``, *optional*):
                New value of the last name; 0-64 characters.

        Returns:
            ``bool``: True on success.
        """
        r = await self.invoke(
            raw.functions.InvokeWithBusinessConnection(
                connection_id=business_connection_id,
                query=raw.functions.account.UpdateProfile(
                    first_name=first_name,
                    last_name=last_name
                )
            )
        )
        return bool(r)
