
from typing import Union, BinaryIO
import pyrogram

class SetMyProfilePhoto:
    async def set_my_profile_photo(
        self: "pyrogram.Client",
        photo: Union[str, BinaryIO] = None,
        video: Union[str, BinaryIO] = None
    ) -> bool:
        """Set your own profile photo or video. Alias for set_profile_photo.


        Parameters:
            photo: Photo file path or binary IO.
            video: Video file path or binary IO.

        Returns:
            ``bool``: True on success.
        """
        return await self.set_profile_photo(photo=photo, video=video)
