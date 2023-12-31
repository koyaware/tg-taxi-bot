import asyncio
import logging

from aiogram import Bot, Dispatcher

from tgbot.config import BOT_TOKEN, storage
from tgbot.filters import register_all_filters
from tgbot.handlers import register_all_handlers

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")

    # storage = MemoryStorage()
    bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)

    register_all_filters(dp)
    register_all_handlers(dp)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")