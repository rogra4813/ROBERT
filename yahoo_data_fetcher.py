import requests
from mongodb import client


def get_price(ticker: str, verbose: bool = False) -> dict:
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    user_agent = {'User-agent': 'Mozilla/5.0'}
    r = requests.get(url=url, headers=user_agent).json()

    aperture = r['chart']['result'][0]['meta']['regularMarketPrice']
    close = r['chart']['result'][0]['meta']['chartPreviousClose']
    currency = r['chart']['result'][0]['meta']['currency']

    if verbose:
        print(f"{ticker}:   {currency} {aperture},  {currency} {close}")
    return {
        "ticker": ticker,
        "b": aperture,
        "a": close,
        "USD": currency
    }


def set_price(document: dict):
    _ = client.get_database('tickers').get_collection('robert').insert_one(document=document)
    return 'ok'
