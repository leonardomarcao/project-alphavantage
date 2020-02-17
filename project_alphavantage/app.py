from .modules.db import Stock, StockImport
from .modules.alpha_vantage_api import AlphaVantageAPI

class App:
    def __init__(self):
        self.stock_list = []
        stock = Stock()
        for stock in stock.get_all_active_stock():
            alpha_vantage_api = AlphaVantageAPI()
            self.stock_list.append(alpha_vantage_api.get_time_series_daily(symbol=stock.symbol))        
