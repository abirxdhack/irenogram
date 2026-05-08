
from typing import Optional, Union

import pyrogram
from pyrogram import raw, types


class SetContactNote:
    async def set_contact_note(
        self: "pyrogram.Client",
        user_id: Union[int, str],
        note: Optional[Union[str, "types.FormattedText"]] = None,
    ):
        """Changes a note of a contact user.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.

            note (``str`` | :obj:`~pyrogram.types.FormattedText`, *optional*):
                Note to set for the user.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                await app.set_contact_note(12345678, types.FormattedText(text="My best friend!"))
        """
        if isinstance(note, str):
            note = types.FormattedText(text=note)

        r = await self.invoke(
            raw.functions.contacts.UpdateContactNote(
                id=await self.resolve_peer(user_id),
                note=await note.write(self)
                if note is not None
                else raw.types.TextWithEntities(text="", entities=[]),
            )
        )

        return r
