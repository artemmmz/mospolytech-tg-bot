"""Main script for start bot."""
import asyncio
import locale
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage

from app.core.redis import redis
from app.core.settings import Mode, settings
from app.handlers import main_router
from app.middlewares.services import ServicesMiddleware


async def main():
    """
    Start bot, init some features.

    :return: NoneType
    """
    log_level = (
        logging.DEBUG if settings.MODE == Mode.development else logging.INFO
    )
    logging.basicConfig(level=log_level)
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

    bot = Bot(
        token=settings.BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
        ),
    )
    # await bot.set_my_commands(all_commands, language_code='ru')
    dp = Dispatcher(storage=RedisStorage(redis))

    services_middleware = ServicesMiddleware()

    dp.message.middleware(services_middleware)
    dp.callback_query.middleware(services_middleware)

    dp.include_router(main_router)

    await dp.start_polling(bot)
    await bot.delete_my_commands()


if __name__ == '__main__':
    asyncio.run(main())
