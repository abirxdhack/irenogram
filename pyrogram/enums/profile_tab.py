
from pyrogram import raw
from .auto_name import AutoName


class ProfileTab(AutoName):
    """Profile tab enumeration used in :obj:`~pyrogram.types.Chat`."""

    POSTS = raw.types.ProfileTabPosts
    "A tab with stories posted by the user or the channel chat and saved to profile."

    GIFTS = raw.types.ProfileTabGifts
    "A tab with gifts received by the user or the channel chat."

    MEDIA = raw.types.ProfileTabMedia
    "A tab with photos and videos posted by the channel."

    FILES = raw.types.ProfileTabFiles
    "A tab with documents posted by the channel."

    LINKS = raw.types.ProfileTabLinks
    "A tab with messages posted by the channel and containing links."

    MUSIC = raw.types.ProfileTabMusic
    "A tab with audio messages posted by the channel."

    VOICE = raw.types.ProfileTabVoice
    "A tab with voice notes posted by the channel."

    GIFS = raw.types.ProfileTabGifs
    "A tab with animations posted by the channel."
