
from pyrogram import types, raw
from ..object import Object


class BusinessIntro(Object):
    """Information about intro of this user.

    Parameters:
        title (``str``, *optional*):
            Title text of the business intro.

        text (``str``, *optional*):
            Message text of the business intro.

        sticker (:obj:`~pyrogram.types.Sticker`, *optional*):
            Sticker of the business intro.

    """

    def __init__(
        self,
        *,
        title: str = None,
        text: str = None,
        sticker: "types.Sticker" = None
    ):
        super().__init__()

        self.title = title
        self.text = text
        self.sticker = sticker


    @staticmethod
    async def _parse(
        client,
        business_intro: "raw.types.BusinessIntro"
    ) -> "BusinessIntro":
        if not business_intro:
            return None
        
        doc = getattr(business_intro, "sticker", None)
        sticker = None

        if doc and isinstance(doc, raw.types.Document):
            sticker = await types.Sticker._parse(
                client,
                doc,
                {type(i): i for i in doc.attributes}
            )

        return BusinessIntro(
            title=getattr(business_intro, "title", None),
            text=getattr(business_intro, "description", None),
            sticker=sticker
        )
