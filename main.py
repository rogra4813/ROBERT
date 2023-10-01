from yahoo_data_fetcher import get_price

tickers = ["BTC-USD", "ETH-USD", "GOLD", "MA"]

for t in tickers:
    get_price(ticker=t, verbose=True)
