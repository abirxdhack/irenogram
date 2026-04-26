
from typing import Union

import pyrogram
from pyrogram import  raw, types

class TranscribeAudio:
    async def transcribe_audio(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int
    ) -> "types.TranscribedAudio":
        """Transcribes the audio of a voice message.


        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            message_id (``int``):
                Identifier of the message containing the voice message.

        Returns:
            :obj:`~pyrogram.types.TranscribeAudio`: On success.
        """
        chat = await self.resolve_peer(chat_id)
        r = await self.invoke(
            raw.functions.messages.TranscribeAudio(
                peer=chat,
                msg_id=message_id
            )
        )

        return types.TranscribedAudio._parse(r)
