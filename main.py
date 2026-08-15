import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from bot.handlers.start import router as start_router
from bot.handlers.trading import router as trading_router

# Load environment variables
load_dotenv()

# Initialize bot and dispatcher
bot = Bot(token=os.getenv("BOT_TOKEN", "dummy_token"))
dp = Dispatcher()

# Include routers
dp.include_router(start_router)
dp.include_router(trading_router)

async def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting bot...")
    # Start polling
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
