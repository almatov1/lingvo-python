from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

language_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🇰🇿 Қазақша",
                callback_data="lang_kk"
            )
        ],
        [
            InlineKeyboardButton(
                text="🇷🇺 Русский",
                callback_data="lang_ru"
            )
        ],
        [
            InlineKeyboardButton(
                text="🇬🇧 English",
                callback_data="lang_en"
            )
        ]
    ]
)
