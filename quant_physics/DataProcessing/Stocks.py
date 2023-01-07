import pandas as pd
import yfinance as yf

class StockDataImporter:
    """
    Points to a stock, and then turns it into a pandas DataFrame
    Input Options:
    * csv_file_path (string) - give path to stock data
    * df (pandas DataFrame) - pre-existing pandas DataFrame containing stock data
    * yf_ticker (string) - ticker of the stock to retrieve data for using yfinance
    """
    def __init__(self, csv_file_path=None, df=None, yf_ticker=None):
        if csv_file_path:
            self.csv_file_path = csv_file_path
            self.stock_df = pd.read_csv(self.csv_file_path)
        elif df is not None:
            self.stock_df = df
        elif yf_ticker is not None:
            # import stock data from yfinance
            yf_stock_data = yf.Ticker(yf_ticker).history(period="max")
            self.stock_df = yf_stock_data
            
class Stock(StockDataImporter):
    '''
    Stock is a wrapper class for stock data
    
    Input:
    * csv_file_path (string) - give path to stock data
    * df (pandas DataFrame) - pre-existing pandas DataFrame containing stock data
    '''
    
    '''
    Attributes
    '''
    strTicker = ""   # string representing stock ticker
    strIndustry = ""  # string representing industry classification    
    
    def __init__(self, csv_file_path=None, df=None, yf_ticker=None):
        super().__init__(csv_file_path=csv_file_path, df=df)
        if yf_ticker:
            self.stock_df = yf_stock_data
        else:
            super().__init__(csv_file_path=csv_file_path, df=df)
    
    def get_opening_price(self, start_date=None, end_date=None):
        '''
        Inputs:
        * start_date
        * end_date
        If these are not specified, it will return all available data.
        '''
        if start_date and end_date:
            df = self.stock_df[(self.stock_df['Date'] >= start_date) & (self.stock_df['Date'] <= end_date)]
        else:
            df = self.stock_df
        return df['Open']
    
    def get_closing_price(self, start_date=None, end_date=None):
        '''
        Inputs:
        * start_date
        * end_date
        If these are not specified, it will return all available data.
        '''
        if start_date and end_date:
            df = self.stock_df[(self.stock_df['Date'] >= start_date) & (self.stock_df['Date'] <= end_date)]
        else:
            df = self.stock_df
        return df['Close']
    
    def get_volume(self, start_date=None, end_date=None):
        '''
        Inputs:
        * start_date
        * end_date
        If these are not specified, it will return all available data.
        '''
        if start_date and end_date:
            df = self.stock_df[(self.stock_df['Date'] >= start_date) & (self.stock_df['Date'] <= end_date)]
        else:
            df = self.stock_df
        return df['Volume']
    
    def get_simple_moving_average(self, window, start_date=None, end_date=None):
        '''
        Inputs:
        * start_date
        * end_date
        '''
        if start_date and end_date:
            df = self.stock_df[(self.stock_df['Date'] >= start_date) & (self.stock_df['Date'] <= end_date)]
        else:
            df = self.stock_df
        return df['Close'].rolling(window=window).mean()
    
    def get_exponential_moving_average(self, window, start_date=None, end_date=None):
        '''
        Inputs:
        * start_date
        * end_date
        '''
        if start_date and end_date:
            df = self.stock_df[(self.stock_df['Date'] >= start_date) & (self.stock_df['Date'] <= end_date)]
        else:
            df = self.stock_df
        return df['Close'].ewm(span=window).mean()
