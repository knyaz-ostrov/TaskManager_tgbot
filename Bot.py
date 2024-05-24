import asyncio

from aiogram import Bot, Dispatcher

from scripts.get_config import GetBotConfig
import scripts.handlers as handlers


async def main() -> None:
    bot = Bot(GetBotConfig().get_token())
    dp = Dispatcher()

    dp.include_router(handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
