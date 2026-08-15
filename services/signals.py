import pandas as pd
import pandas_ta as ta

def analyze_signals(ohlcv_data):
    if not ohlcv_data:
        return "No data available."
        
    df = pd.DataFrame(ohlcv_data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    
    # Calculate RSI (Relative Strength Index)
    df.ta.rsi(length=14, append=True)
    
    # Calculate MACD
    df.ta.macd(fast=12, slow=26, signal=9, append=True)
    
    latest = df.iloc[-1]
    
    rsi_val = latest.get('RSI_14', 50)
    macd_val = latest.get('MACD_12_26_9', 0)
    macd_signal = latest.get('MACDs_12_26_9', 0)
    
    signal = "NEUTRAL"
    if rsi_val < 30 and macd_val > macd_signal:
        signal = "STRONG BUY 🟢"
    elif rsi_val > 70 and macd_val < macd_signal:
        signal = "STRONG SELL 🔴"
    elif rsi_val < 40:
        signal = "BUY 🟢"
    elif rsi_val > 60:
        signal = "SELL 🔴"
        
    return {
        "rsi": round(rsi_val, 2),
        "macd": round(macd_val, 2),
        "signal": signal,
        "price": latest['close']
    }
