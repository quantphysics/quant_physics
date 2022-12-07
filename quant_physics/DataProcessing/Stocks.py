import pandas as pd

class StockDataImporter:
    """
    Points to a stock, and then turns it into a pandas DataFrame

    Input:
    * csv_file_path (string) - give path to stock data
    """
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
    
    def import_data(self):
        self.df = pd.read_csv(self.csv_file_path)

class Stock(StockDataImporter):
    '''
    Stock is a wrapper for stock data
    Inherits StockDataImporter
    
    Input:
    * csv_file_path (string) - give path to stock data
    '''
    def __init__(self, csv_file_path):
        super().__init__(csv_file_path)
        self.import_data()
    
    def get_opening_price(self, start_date=None, end_date=None):
        if start_date and end_date:
            df = self.df[(self.df['Date'] >= start_date) & (self.df['Date'] <= end_date)]
        else:
            df = self.df
        return df['Open'].iloc[0]
    
    def get_closing_price(self, start_date=None, end_date=None):
        if start_date and end_date:
            df = self.df[(self.df['Date'] >= start_date) & (self.df['Date'] <= end_date)]
        else:
            df = self.df
        return df['Close'].iloc[-1]
    
    def get_simple_moving_average(self, window, start_date=None, end_date=None):
        if start_date and end_date:
            df = self.df[(self.df['Date'] >= start_date) & (self.df['Date'] <= end_date)]
        else:
            df = self.df
        return df['Close'].rolling(window=window).mean()
    
    def get_exponential_moving_average(self, window, start_date=None, end_date=None):
        if start_date and end_date:
            df = self.df[(self.df['Date'] >= start_date) & (self.df['Date'] <= end_date)]
        else:
            df = self.df
        return df['Close'].ewm(span=window).mean()
