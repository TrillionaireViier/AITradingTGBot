from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "👋 Welcome to AITradingTGBot!\n\n"
        "I am your AI-powered cryptocurrency trading assistant.\n\n"
        "Features:\n"
        "📈 Get trading signals\n"
        "🤖 AI Market Analysis\n"
        "💰 Execute trades directly on Binance/Bybit\n\n"
        "Use /help to see available commands."
    )

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "Available commands:\n"
        "/start - Start the bot\n"
        "/signals - Get current market signals\n"
        "/trade - Open a position\n"
        "/settings - Configure API keys"
    )
