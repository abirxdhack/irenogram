
from typing import Optional, Union

import pyrogram
from pyrogram import raw, types


class ComposeTextWithAI:
    async def compose_text_with_ai(
        self: "pyrogram.Client",
        text: Union[str, "types.FormattedText"],
        translate_to_language_code: Optional[str],
        style_name: Optional[str] = None,
        add_emojis: Optional[bool] = None,
    ) -> "types.FormattedText":
        """Changes text using an AI model.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            text (``str`` | :obj:`~pyrogram.types.FormattedText`):
                The original text.

            translate_to_language_code (``str``, *optional*):
                Pass a language code to which the text will be translated.
                Must be one of "af", "sq", "am", "ar", "hy", "az", "eu", "be", "bn", "bs", "bg", "ca", "ceb", "zh-CN", "zh", "zh-Hans", "zh-TW", "zh-Hant", "co", "hr", "cs", "da", "nl", "en", "eo", "et",
                "fi", "fr", "fy", "gl", "ka", "de", "el", "gu", "ht", "ha", "haw", "he", "iw", "hi", "hmn", "hu", "is", "ig", "id", "in", "ga", "it", "ja", "jv", "kn", "kk", "km", "rw", "ko",
                "ku", "ky", "lo", "la", "lv", "lt", "lb", "mk", "mg", "ms", "ml", "mt", "mi", "mr", "mn", "my", "ne", "no", "ny", "or", "ps", "fa", "pl", "pt", "pa", "ro", "ru", "sm", "gd", "sr",
                "st", "sn", "sd", "si", "sk", "sl", "so", "es", "su", "sw", "sv", "tl", "tg", "ta", "tt", "te", "th", "tr", "tk", "uk", "ur", "ug", "uz", "vi", "cy", "xh", "yi", "ji", "yo", "zu"

            style_name (``str``, *optional*):
                Name of the style of the resulted text.

            add_emojis (``bool``, *optional*):
                Pass True to add emoji to the text.

        Returns:
            :obj:`~pyrogram.types.FormattedText`: On success, information about the composed text is returned.
        """
        if isinstance(text, str):
            text = types.FormattedText(text=text)

        r = await self.invoke(
            raw.functions.messages.ComposeMessageWithAI(
                text=await text.write(self),
                translate_to_lang=translate_to_language_code,
                change_tone=style_name,
                emojify=add_emojis,
            )
        )

        return types.FormattedText._parse(self, r.result_text)
