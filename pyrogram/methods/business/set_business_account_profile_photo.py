
from typing import Union, BinaryIO, Optional

import pyrogram
from pyrogram import raw

class SetBusinessAccountProfilePhoto:
    async def set_business_account_profile_photo(
        self: "pyrogram.Client",
        business_connection_id: str,
        photo: Optional[Union[str, BinaryIO]] = None,
        video: Optional[Union[str, BinaryIO]] = None,
        is_public: Optional[bool] = None
    ) -> bool:
        """Sets the profile photo of a managed business account.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            business_connection_id (``str``):
                Unique identifier of the business connection.

            photo (``str`` | ``BinaryIO``, *optional*):
                Profile photo to set. File path or binary IO.

            video (``str`` | ``BinaryIO``, *optional*):
                Profile video to set. File path or binary IO.

            is_public (``bool``, *optional*):
                Pass True to set the public photo.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.set_business_account_profile_photo(connection_id, photo="photo.jpg")

                await app.set_business_account_profile_photo(connection_id, video="video.mp4")
        """
        if photo:
            file = await self.save_file(photo)
            r = await self.invoke(
                raw.functions.InvokeWithBusinessConnection(
                    connection_id=business_connection_id,
                    query=raw.functions.photos.UploadProfilePhoto(
                        file=file,
                        fallback=not is_public if is_public is not None else None
                    )
                )
            )
        elif video:
            file = await self.save_file(video)
            r = await self.invoke(
                raw.functions.InvokeWithBusinessConnection(
                    connection_id=business_connection_id,
                    query=raw.functions.photos.UploadProfilePhoto(
                        video=file,
                        fallback=not is_public if is_public is not None else None
                    )
                )
            )
        else:
            raise ValueError("Either photo or video must be provided")

        return bool(r)
