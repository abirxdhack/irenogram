
from typing import Union, AsyncGenerator, Optional
import pyrogram
from pyrogram import raw, types

class GetUserProfileAudios:
    async def get_user_profile_audios(
        self: "pyrogram.Client",
        user_id: Union[int, str],
        limit: int = 0,
        offset: int = 0
    ) -> AsyncGenerator["types.Audio", None]:
        """Get a user's profile audio files (voice messages set as profile).


        Parameters:
            user_id: Target user.
            limit: Max number of audios. 0 = all.
            offset: Offset.

        Returns:
            Generator of :obj:`~pyrogram.types.Audio`.
        """
        peer = await self.resolve_peer(user_id)
        current = 0
        total = abs(limit) or (1 << 31) - 1
        fetch_limit = min(100, total)

        while True:
            r = await self.invoke(
                raw.functions.photos.GetUserPhotos(
                    user_id=peer,
                    offset=offset,
                    max_id=0,
                    limit=fetch_limit
                )
            )
            audios = getattr(r, "photos", [])
            if not audios:
                return
            for audio in audios:
                yield audio
                current += 1
                offset += 1
                if current >= total:
                    return
            if len(audios) < fetch_limit:
                return
