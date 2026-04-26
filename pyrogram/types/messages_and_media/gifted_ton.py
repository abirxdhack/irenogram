
import random

from pyrogram import raw, types

from ..object import Object


class GiftedTon(Object):
    """Toncoins were gifted to a user.

    Parameters:
        gifter (:obj:`~pyrogram.types.User`, *optional*):
            User that gifted Telegram Premium.
            None if the gift was anonymous.

        receiver (:obj:`~pyrogram.types.User`):
            User that received Telegram Premium.

        ton_amount (``int``):
            The received amount of Toncoins, in the smallest units of the cryptocurrency.

        transaction_id (``str``, *optional*):
            Identifier of the transaction for Telegram Stars purchase.
            For receiver only.

        sticker (:obj:`~pyrogram.types.Sticker`):
            A sticker to be shown in the message.
    """
    def __init__(
        self,
        *,
        gifter: "types.User" = None,
        receiver: "types.User",
        ton_amount: int = None,
        transaction_id: str = None,
        sticker: "types.Sticker" = None,
    ):
        super().__init__()

        self.gifter = gifter
        self.receiver = receiver
        self.ton_amount = ton_amount
        self.transaction_id = transaction_id
        self.sticker = sticker

    @staticmethod
    async def _parse(
        client,
        action: "raw.types.MessageActionGiftTon",
        gifter: "raw.base.User" = None,
        receiver: "raw.base.User" = None,
    ) -> "GiftedTon":
        raw_stickers = await client.invoke(
            raw.functions.messages.GetStickerSet(
                stickerset=raw.types.InputStickerSetTonGifts(),
                hash=0
            )
        )

        return GiftedTon(
            gifter=types.User._parse(client, gifter),
            receiver=types.User._parse(client, receiver),
            ton_amount=action.crypto_amount,
            transaction_id=action.transaction_id,
            sticker=random.choice(
                types.List(
                    [
                        await types.Sticker._parse(
                            client,
                            doc,
                            {
                                type(i): i for i in doc.attributes
                            }
                        ) for doc in raw_stickers.documents
                    ]
                )
            )
        )
