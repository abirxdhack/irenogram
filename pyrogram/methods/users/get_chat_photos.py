
from datetime import datetime
from typing import Union, AsyncGenerator, Optional

import pyrogram
from pyrogram import types, raw, utils


class GetChatPhotos:
    async def get_chat_photos(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        limit: int = 0,
    ) -> Optional[
        Union[
            AsyncGenerator["types.Photo", None],
            AsyncGenerator["types.Animation", None]
        ]
    ]:
        """Get a chat or a user profile photos sequentially.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            limit (``int``, *optional*):
                Limits the number of profile photos to be retrieved.
                By default, no limit is applied and all profile photos are returned.

        Returns:
            ``Generator``: A generator yielding :obj:`~pyrogram.types.Photo` | :obj:`~pyrogram.types.Animation` objects.

        Example:
            .. code-block:: python

                async for photo in app.get_chat_photos("me"):
                    print(photo)
        """
        peer_id = await self.resolve_peer(chat_id)

        if isinstance(peer_id, raw.types.InputPeerChannel):
            r = await self.invoke(
                raw.functions.channels.GetFullChannel(
                    channel=peer_id
                )
            )

            current = types.Animation._parse_chat_animation(
                self,
                r.full_chat.chat_photo,
                f"photo_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.mp4"
            ) or types.Photo._parse(self, r.full_chat.chat_photo) or []

            if current:
                current = [current]

            if not self.me.is_bot:
                r = await utils.parse_messages(
                    self,
                    await self.invoke(
                        raw.functions.messages.Search(
                            peer=peer_id,
                            q="",
                            filter=raw.types.InputMessagesFilterChatPhotos(),
                            min_date=0,
                            max_date=0,
                            offset_id=0,
                            add_offset=0,
                            limit=limit or (1 << 31) - 1,
                            max_id=0,
                            min_id=0,
                            hash=0
                        )
                    )
                )

                extra = [message.new_chat_photo for message in r]

                if extra:
                    if current:
                        current.extend(extra)
                    else:
                        current = extra

            count = 0

            for photo in current:
                yield photo

                count += 1

                if limit and count >= limit:
                    return
        else:
            r = await self.invoke(
                raw.functions.photos.GetUserPhotos(
                    user_id=peer_id,
                    offset=0,
                    max_id=0,
                    limit=limit or (1 << 31) - 1
                )
            )

            count = 0

            for photo in r.photos:
                yield types.Photo._parse(self, photo)

                count += 1

                if limit and count >= limit:
                    return
