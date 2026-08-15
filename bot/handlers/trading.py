from aiogram import Router, types
from aiogram.filters import Command
from services.exchange import ExchangeService
from services.signals import analyze_signals
from services.ai_analyzer import get_market_sentiment

router = Router()

# Default to Bybit as requested (BingX is also supported by ccxt)
exchange_service = ExchangeService(exchange_id='bybit')

@router.message(Command("signals"))
async def cmd_signals(message: types.Message):
    # Fetch BTC/USDT data
    await message.answer("🔄 Fetching data and analyzing market... please wait.")
    
    ohlcv = exchange_service.fetch_ohlcv('BTC/USDT', '1h', limit=50)
    if not ohlcv:
        await message.answer("❌ Failed to fetch data from exchange.")
        return
        
    analysis = analyze_signals(ohlcv)
    
    msg = (
        f"📊 **BTC/USDT Market Data (Bybit)**\n"
        f"Price: ${analysis['price']}\n"
        f"RSI (14): {analysis['rsi']}\n"
        f"MACD: {analysis['macd']}\n"
        f"Technical Signal: **{analysis['signal']}**\n\n"
        f"🤖 *Asking ChatGPT for free analysis...*"
    )
    
    sent_msg = await message.answer(msg, parse_mode="Markdown")
    
    # Get free AI analysis
    ai_summary = await get_market_sentiment('BTC', analysis['price'], analysis['signal'])
    
    final_msg = msg.replace("🤖 *Asking ChatGPT for free analysis...*", f"🤖 **AI Analysis:**\n{ai_summary}")
    
    await sent_msg.edit_text(final_msg, parse_mode="Markdown")
