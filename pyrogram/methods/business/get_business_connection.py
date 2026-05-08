
import pyrogram
from pyrogram import raw, types


class GetBusinessConnection:
    async def get_business_connection(
        self: "pyrogram.Client",
        business_connection_id: str
    ):
        """Use this method to get information about the connection of the bot with a business account.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            business_connection_id (``str``):
                Unique identifier of the business connection.

        Returns:
            :obj:`~pyrogram.types.BusinessConnection`: On success the business connection is returned.

        Example:
            .. code-block:: python

                await app.get_business_connection(business_connection_id)
        """
        r = await self.invoke(
            raw.functions.account.GetBotBusinessConnection(
                connection_id=business_connection_id
            )
        )

        users = {i.id: i for i in r.users}

        return types.BusinessConnection._parse(self, r.updates[0].connection, users)
