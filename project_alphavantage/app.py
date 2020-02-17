from .modules.db import Stock, StockImport
from .modules.alpha_vantage_api import AlphaVantageAPI

class App:
    def __init__(self):        
        stock = Stock()
        for stock in stock.get_all_active_stock():
            alpha_vantage_api = AlphaVantageAPI()
            stock_import = alpha_vantage_api.get_time_series_daily(symbol=stock.symbol)
            for day, values in stock_import.items():
                StockImport.save_or_update_stock_imports(date=day, close=float(values.get('4. close')), stock=stock)
