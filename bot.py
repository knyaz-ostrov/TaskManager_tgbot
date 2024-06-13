"""
Модуль для запуска телеграм-бота.
"""
import asyncio

from misc import bot, dp


async def main() -> None:
    """
    Запуск бота.
    
    :return:
    """
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
