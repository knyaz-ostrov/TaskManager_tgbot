"""
Модуль для запуска телеграм-бота.
"""
import asyncio
import logging

from aiogram import Bot, Dispatcher


from handlers import general
from data.scripts.config import BotConfig
from constants import LOG_BOT_START, LOG_FILE_NAME, LOG_FORMAT


@logging.info(LOG_BOT_START, BotConfig.token)
async def main() -> None:
    """
    Указывает токен для телеграм-бота, добавляет все роутеры из директории handlers, удаляет все
    события, произошедшие во время неактивности бота, запускает бота.
    
    :return:
    """
    bot = Bot(BotConfig.token)
    dp = Dispatcher()

    dp.include_router(general.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        filename=LOG_FILE_NAME,
        filemode="w",
        format=LOG_FORMAT,
        encoding='UTF-8'
    )

    asyncio.run(main())
