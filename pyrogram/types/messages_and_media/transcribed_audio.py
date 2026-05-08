
from pyrogram import  raw
from ..object import Object

class TranscribedAudio(Object):
    """Transcribes the audio of a voice message.


    Parameters:
        transcription_id (``int``):
            Unique identifier of the transcription.

        text (``str``):
            Transcribed text.

        pending (``bool``, *optional*):
            Whether the transcription is pending.

        trial_remains_num (``int``, *optional*):
            Number of trials remaining.

        trial_remains_until_date (``int``, *optional*):
            Date the trial remains until.
    """

    def __init__(
        self,
        *,
        transcription_id: int,
        text: str,
        pending: bool = None,
        trial_remains_num: int = None,
        trial_remains_until_date: int = None
    ):
        self.transcription_id = transcription_id
        self.text = text
        self.pending = pending
        self.trial_remains_num = trial_remains_num
        self.trial_remains_until_date = trial_remains_until_date

    @staticmethod
    def _parse(transcribe_result: "raw.types.messages.TranscribedAudio") -> "TranscribedAudio":
        return TranscribedAudio(
            transcription_id=transcribe_result.transcription_id,
            text=transcribe_result.text,
            pending=transcribe_result.pending,
            trial_remains_num=transcribe_result.trial_remains_num,
            trial_remains_until_date=transcribe_result.trial_remains_until_date
        )
