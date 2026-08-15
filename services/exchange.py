import ccxt

class ExchangeService:
    def __init__(self, exchange_id='binance', api_key=None, secret=None):
        exchange_class = getattr(ccxt, exchange_id)
        self.exchange = exchange_class({
            'apiKey': api_key,
            'secret': secret,
            'enableRateLimit': True,
        })
        
    def fetch_price(self, symbol='BTC/USDT'):
        try:
            ticker = self.exchange.fetch_ticker(symbol)
            return ticker['last']
        except Exception as e:
            return str(e)
            
    def fetch_ohlcv(self, symbol='BTC/USDT', timeframe='1h', limit=100):
        try:
            return self.exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
        except Exception as e:
            return None
