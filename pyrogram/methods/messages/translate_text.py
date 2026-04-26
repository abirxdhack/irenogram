
from typing import List, Optional, Union

import pyrogram
from pyrogram import enums, raw, types, utils


class TranslateText:
    async def translate_text(
        self: "pyrogram.Client",
        text: Union[str, "types.FormattedText"],
        to_language_code: str,
        tone: Optional[str] = None,
    ) -> "types.FormattedText":
        """Translate a text to the given language.

        If the current user is a Telegram Premium user, then text formatting is preserved.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            text (``str`` | :obj:`~pyrogram.types.FormattedText`):
                Text to translate.

            to_language_code (``str``):
                Language code of the language to which the message is translated.
                Must be one of "af", "sq", "am", "ar", "hy", "az", "eu", "be", "bn", "bs", "bg", "ca", "ceb", "zh-CN", "zh", "zh-Hans", "zh-TW", "zh-Hant", "co", "hr", "cs", "da", "nl", "en", "eo", "et",
                "fi", "fr", "fy", "gl", "ka", "de", "el", "gu", "ht", "ha", "haw", "he", "iw", "hi", "hmn", "hu", "is", "ig", "id", "in", "ga", "it", "ja", "jv", "kn", "kk", "km", "rw", "ko",
                "ku", "ky", "lo", "la", "lv", "lt", "lb", "mk", "mg", "ms", "ml", "mt", "mi", "mr", "mn", "my", "ne", "no", "ny", "or", "ps", "fa", "pl", "pt", "pa", "ro", "ru", "sm", "gd", "sr",
                "st", "sn", "sd", "si", "sk", "sl", "so", "es", "su", "sw", "sv", "tl", "tg", "ta", "tt", "te", "th", "tr", "tk", "uk", "ur", "ug", "uz", "vi", "cy", "xh", "yi", "ji", "yo", "zu"

            tone (``str``, *optional*):
                Tone of the translation.
                Must be one of "formal", "neutral", "casual".

        Returns:
            :obj:`~pyrogram.types.FormattedText`: On success, information about the translated text is returned.

        Example:
            .. code-block:: python

                await app.translate_text("Hello!", "ru")
        """
        if isinstance(text, str):
            text = types.FormattedText(text=text)

        r = await self.invoke(
            raw.functions.messages.TranslateText(
                to_lang=to_language_code,
                text=[await text.write(self)],
                tone=tone
            )
        )

        return types.FormattedText._parse(self, r.result[0])
