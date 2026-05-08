
import pyrogram
from pyrogram import raw, utils
from pyrogram.file_id import FileType


class RemoveProfileAudio:
    async def remove_profile_audio(self: "pyrogram.Client", file_id: str):
        """Removes an audio file from the profile audio files of the current user.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            file_id (``str``):
                Identifier of the audio file to be removed.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                await app.remove_profile_audio(file_id)
        """
        r = await self.invoke(
            raw.functions.account.SaveMusic(
                id=(utils.get_input_media_from_file_id(file_id, FileType.AUDIO)).id,
                unsave=True
            )
        )

        return r
