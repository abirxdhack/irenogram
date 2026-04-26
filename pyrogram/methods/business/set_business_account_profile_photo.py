
from typing import Union, BinaryIO

import pyrogram
from pyrogram import raw

class SetBusinessAccountProfilePhoto:
    async def set_business_account_profile_photo(
        self: "pyrogram.Client",
        business_connection_id: str,
        photo: Union[str, BinaryIO] = None,
        video: Union[str, BinaryIO] = None,
        is_public: bool = None
    ) -> bool:
        """Sets the profile photo of a managed business account.


        Parameters:
            business_connection_id (``str``): Unique identifier of the business connection.
            photo (``str`` | ``BinaryIO``, *optional*): Photo to set. File path or binary IO.
            video (``str`` | ``BinaryIO``, *optional*): Video to set. File path or binary IO.
            is_public (``bool``, *optional*): Pass True to set the public photo.

        Returns:
            ``bool``: True on success.
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
