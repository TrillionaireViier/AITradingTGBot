import g4f

async def get_market_sentiment(coin: str, current_price: float, technical_signal: str) -> str:
    """
    Uses g4f (free ChatGPT API alternative) to generate a quick market analysis.
    """
    prompt = f"Act as an expert crypto trader. Analyze {coin}. The current price is {current_price}. Technical analysis says: {technical_signal}. Write a short 3-sentence summary of what you think about this coin right now based on this data. Keep it professional but engaging."
    
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.gpt_35_turbo,
            messages=[{"role": "user", "content": prompt}]
        )
        return response
    except Exception as e:
        return f"AI Analysis currently unavailable. Error: {str(e)}"
