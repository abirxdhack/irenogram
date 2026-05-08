
import pyrogram
from pyrogram import raw

class GetManagedBotToken:
    async def get_managed_bot_token(
        self: "pyrogram.Client",
        bot_id: int,
        revoke: bool = False,
    ) -> str:
        """Fetch the HTTP Bot API token for a managed bot.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            bot_id (``int``):
                Identifier of the managed bot whose token to retrieve.

            revoke (``bool``, *optional*):
                Pass True to revoke the existing token and generate a new one.
                Defaults to False.

        Returns:
            ``str``: The bot token string in the standard ``123456:ABC-DEF`` format.

        Example:
            .. code-block:: python

                token = await app.get_managed_bot_token(bot_id=123456789)
                print(token)
        """
        bot_peer = await self.resolve_peer(bot_id)

        r = await self.invoke(
            raw.functions.bots.ExportBotToken(
                bot=bot_peer,
                revoke=revoke,
            )
        )

        return r.token
