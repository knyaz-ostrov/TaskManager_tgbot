import asyncio
import logging

from aiogram import Bot, Dispatcher


from data.scripts.config import BotConfig
from handlers import general



async def main() -> None:
    bot = Bot(BotConfig.token)
    dp = Dispatcher()

    dp.include_router(general.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        filename="log.log",
        filemode="w",
        format="%(asctime)s %(levelname)s %(message)s",
        encoding='UTF-8'
    )

    asyncio.run(main())
