


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PageBlock = Union[raw.types.PageBlockAnchor, raw.types.PageBlockAudio, raw.types.PageBlockAuthorDate, raw.types.PageBlockBlockquote, raw.types.PageBlockChannel, raw.types.PageBlockCollage, raw.types.PageBlockCover, raw.types.PageBlockDetails, raw.types.PageBlockDivider, raw.types.PageBlockEmbed, raw.types.PageBlockEmbedPost, raw.types.PageBlockFooter, raw.types.PageBlockHeader, raw.types.PageBlockKicker, raw.types.PageBlockList, raw.types.PageBlockMap, raw.types.PageBlockOrderedList, raw.types.PageBlockParagraph, raw.types.PageBlockPhoto, raw.types.PageBlockPreformatted, raw.types.PageBlockPullquote, raw.types.PageBlockRelatedArticles, raw.types.PageBlockSlideshow, raw.types.PageBlockSubheader, raw.types.PageBlockSubtitle, raw.types.PageBlockTable, raw.types.PageBlockTitle, raw.types.PageBlockUnsupported, raw.types.PageBlockVideo]


class PageBlock:
    """Telegram API base type.

    Constructors:
        This base type has 29 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PageBlockAnchor
            PageBlockAudio
            PageBlockAuthorDate
            PageBlockBlockquote
            PageBlockChannel
            PageBlockCollage
            PageBlockCover
            PageBlockDetails
            PageBlockDivider
            PageBlockEmbed
            PageBlockEmbedPost
            PageBlockFooter
            PageBlockHeader
            PageBlockKicker
            PageBlockList
            PageBlockMap
            PageBlockOrderedList
            PageBlockParagraph
            PageBlockPhoto
            PageBlockPreformatted
            PageBlockPullquote
            PageBlockRelatedArticles
            PageBlockSlideshow
            PageBlockSubheader
            PageBlockSubtitle
            PageBlockTable
            PageBlockTitle
            PageBlockUnsupported
            PageBlockVideo
    """

    QUALNAME = "pyrogram.raw.base.PageBlock"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/page-block")
