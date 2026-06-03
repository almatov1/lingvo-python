from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.language import language_keyboard

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        text=(
            "Сәлеметсіз бе!\n\n"
            "Добро пожаловать в курс казахского языка.\n\n"
            "Выберите язык интерфейса:"
        ),
        reply_markup=language_keyboard
    )
    