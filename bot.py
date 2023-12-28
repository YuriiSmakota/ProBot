import logging
import asyncio

from aiogram import Dispatcher, Bot
from settings import config

from heandlers import command_start, invite_query


async def main():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

    bot = Bot(token=config.token.get_secret_value(), parse_mode="html")
    dp = Dispatcher()

    dp.include_router(command_start.router)
    dp.include_router(invite_query.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
