import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from app.core.settings import settings, Mode
from app.handlers import main_router


async def main():
    logging.basicConfig(level=logging.DEBUG)

    bot = Bot(
        token=settings.BOT_TOKEN
    )
    dp = Dispatcher(
        storage=MemoryStorage()
    )
    dp.include_router(main_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
