import asyncio
import os

from dotenv import load_dotenv

from aiogram import Bot
from aiogram import Dispatcher

from handlers.start import router as start_router

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def main():
    bot = Bot(TOKEN)

    dp = Dispatcher()

    dp.include_router(start_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
    