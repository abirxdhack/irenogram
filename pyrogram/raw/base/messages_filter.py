


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

MessagesFilter = Union[raw.types.InputMessagesFilterChatPhotos, raw.types.InputMessagesFilterContacts, raw.types.InputMessagesFilterDocument, raw.types.InputMessagesFilterEmpty, raw.types.InputMessagesFilterGeo, raw.types.InputMessagesFilterGif, raw.types.InputMessagesFilterMusic, raw.types.InputMessagesFilterMyMentions, raw.types.InputMessagesFilterPhoneCalls, raw.types.InputMessagesFilterPhotoVideo, raw.types.InputMessagesFilterPhotos, raw.types.InputMessagesFilterPinned, raw.types.InputMessagesFilterPoll, raw.types.InputMessagesFilterRoundVideo, raw.types.InputMessagesFilterRoundVoice, raw.types.InputMessagesFilterUrl, raw.types.InputMessagesFilterVideo, raw.types.InputMessagesFilterVoice]


class MessagesFilter:
    """Telegram API base type.

    Constructors:
        This base type has 18 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputMessagesFilterChatPhotos
            InputMessagesFilterContacts
            InputMessagesFilterDocument
            InputMessagesFilterEmpty
            InputMessagesFilterGeo
            InputMessagesFilterGif
            InputMessagesFilterMusic
            InputMessagesFilterMyMentions
            InputMessagesFilterPhoneCalls
            InputMessagesFilterPhotoVideo
            InputMessagesFilterPhotos
            InputMessagesFilterPinned
            InputMessagesFilterPoll
            InputMessagesFilterRoundVideo
            InputMessagesFilterRoundVoice
            InputMessagesFilterUrl
            InputMessagesFilterVideo
            InputMessagesFilterVoice
    """

    QUALNAME = "pyrogram.raw.base.MessagesFilter"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/messages-filter")
