""" Market Service """
"""_summary_
this file to write any business logic for the Market
"""

import requests

API_KEY = "95f87c03d3d5432c8f4df7657157bbc9"
SYMBOLS = ["AAPL", "MSFT", "GOOG", "AMZN", "META"]

def get_market_data():
    url = f"https://api.twelvedata.com/time_series?symbol={','.join(SYMBOLS)}&interval=1min&apikey={API_KEY}&timezone=utc&outputsize=1"

    try:
        response = requests.get(url)
        data = response.json()
        if data.get('status', 'ok') == 'error':
            raise ValueError("Received no data for the given symbol.")
        return data
    except Exception as e:
        print("error raised")
        return None
