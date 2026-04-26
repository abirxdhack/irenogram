
import pyrogram
from pyrogram import raw

class DeletePasskey:
    async def delete_passkey(
        self: "pyrogram.Client",
        passkey_id: str,
    ) -> bool:
        """Delete a registered passkey from the current account.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            passkey_id (``str``):
                The unique credential ID of the passkey to delete.
                Obtain this from :meth:`~pyrogram.Client.get_passkeys`.

        Returns:
            ``bool``: True on success.

        Raises:
            :class:`~pyrogram.errors.RPCError`: On Telegram API error.

        Example:
            .. code-block:: python


                await app.delete_passkey(passkey_id="abc123")


                passkeys = await app.get_passkeys()
                for pk in passkeys:
                    await app.delete_passkey(pk.id)
        """
        return await self.invoke(
            raw.functions.account.DeletePasskey(id=passkey_id)
        )
