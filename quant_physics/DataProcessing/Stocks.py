import pandas as pd

class StockDataImporter:
    """
    Points to a stock, and then turns it into a pandas DataFrame

    Input:
    * csv_file_path (string) - give path to stock data
    * df (pandas DataFrame) - pre-existing pandas DataFrame containing stock data
    """
    def __init__(self, csv_file_path=None, df=None):
        if csv_file_path:
            self.csv_file_path = csv_file_path
            self.stock_df = pd.read_csv(self.csv_file_path)
        elif df is not None:
            self.stock_df = df

class Stock(StockDataImporter):
    '''
    Stock is a wrapper class for stock data
    
    Input:
    * csv_file_path (string) - give path to stock data
    * df (pandas DataFrame) - pre-existing pandas DataFrame containing stock data
    '''
    def __init__(self, csv_file_path=None, df=None):
        super().__init__(csv_file_path=csv_file_path, df=df)
    
    def get_opening_price(self, start_date=None, end_date=None):
        if start_date and end_date:
            df = self.stock_df[(self.stock_df['Date'] >= start_date) & (self.stock_df['Date'] <= end_date)]
        else:
            df = self.stock_df
        return df['Open'].iloc[0]
    
    def get_closing_price(self, start_date=None, end_date=None):
        if start_date and end_date:
            df = self.stock_df[(self.stock_df['Date'] >= start_date) & (self.stock_df['Date'] <= end_date)]
        else:
            df = self.stock_df
        return df['Close'].iloc[-1]
    
    def get_simple_moving_average(self, window, start_date=None, end_date=None):
        if start_date and end_date:
            df = self.stock_df[(self.stock_df['Date'] >= start_date) & (self.stock_df['Date'] <= end_date)]
        else:
            df = self.stock_df
        return df['Close'].rolling(window=window).mean()
    
    def get_exponential_moving_average(self, window, start_date=None, end_date=None):
        if start_date and end_date:
            df = self.stock_df[(self.stock_df['Date'] >= start_date) & (self.stock_df['Date'] <= end_date)]
        else:
            df = self.stock_df
        return df['Close'].ewm(span=window).mean()
