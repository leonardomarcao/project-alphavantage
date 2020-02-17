import requests as req
import json
from project_alphavantage.config.base import (
    ALPHA_VANTAGE_API_KEY,
    ALPHA_VANTAGE_API_URL
)

class AlphaVantageAPI:            

    def __init__(self):
        self.api_url = f'{ALPHA_VANTAGE_API_URL}'

    def get_time_series_daily(self, symbol: str, datatype: str = 'json'):
        return json.loads(req.get(url=self.api_url+'query', 
                                  params={'symbol': f'{symbol}',
                                          'function': 'TIME_SERIES_DAILY',
                                          'apikey': f'{self.api_key()}'}).text)['Time Series (Daily)']

    @property
    def api_url(self):
        return self._api_url

    @api_url.setter
    def api_url(self, v):
        self._api_url = v

    @classmethod
    def api_key(cls):
        return ALPHA_VANTAGE_API_KEY
