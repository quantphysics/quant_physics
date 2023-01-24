import pandas as pd
import json
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from Transactions import Transaction
from Stocks import Stock
from Transactions import Transaction
from Stocks import Stock

class Portfolio:
    
    def __init__(self):
        self.transactions = [] # list to store transaction history
        self.base_url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-financials"
        self.assets = {} # dictionary to store Stock object and quantity
        self.balance = 0  # current total value of portfolio
    
    # parameters: string filename
    # return: 0
    # action: writes transactions and assets to JSON file
    def exportJSON(self, filename):
        # store the transactions and assets in a JSON object
        json_data = json.dumps({
            'transactions': self.transactions,
            'assets': self.assets
        })

        # write JSON object to file
        with open(filename, 'w') as outfile:
            outfile.write(json_data)
            
        return 0
    
    # parameters: string filename
    # return: portfolio object
    # imports Portfolio from a JSON file
    def importJSON(self, filename):
        # read JSON data from the file
        with open(filename, 'r') as infile:
            json_data = infile.read()
        
        # deserialize JSON data
        data = json.loads(json_data)
        
        # create new Portfolio object with the deserialized data
        portfolio = Portfolio()
        portfolio.transactions = data['transactions']
        portfolio.assets = data['assets']
        
        return portfolio
      
    # parameters: string ticker, int quantity
    # return: 0
    # action: updates transactions and assets for a purchase
    # parameters: string ticker, int quantity, purchase time
    # return: 0
    # action: updates transactions and assets for a purchase
    def buy(self,ticker, quantity, purchase_time):    
        # update assets
        if ticker in self.assets:
            self.assets[stock] += quantity
        else:
            stock = Stock(yf_ticker = ticker)  # create Stock object with this ticker
            self.assets[stock] = quantity
        price = stock.get_price(transaction_date=purchase_time) # buy based on opening price
        self.transactions.append({"type": "buy" , "ticker": ticker, "quantity": quantity, 
                                  "price": price, "time": purchase_time})
        balance += price * quantity
        return 0
    
    # parameters: string ticker, int quantity
    # return: 0
    # action: updates transactions and assets for a sale
    def sell(self, ticker, quantity, purchase_time):
        # check if you own any of this stock
        
        
        # UNFUCK THIS LATER
        if ticker in self.assets:
            if self.assets[stock] >= quantity:
                self.assets[stock] -= quantity
            else:
                raise Exception("You only own " self.assets[stock] " of {}".format(ticker))
        else: 
            raise Exception("You do not own any shares of {}".format(ticker))
        
        price = stock.get_price(transaction_date=purchase_time) # buy based on opening price

        # update assets
        self.transactions.append({"type": "sell" , "ticker": ticker, "quantity": quantity, 
                                  "price": price, "time": purchase_time})
        return 0
    
    # parameters: string ticker
    # return: quantity of specified stock currently in portfolio
    # counts quantity of stock purchased by viewing transaction history
    def stockQuantity(self, ticker):
        # check if you own any of this stock
        if ticker in self.assets:
             self.assets[ticker] -= quantity
        else: 
              raise Exception("You do not own any shares of {}".format(ticker))
        
        # add up stock quantity using transaction history
        quantity = 0
        for transaction in self.transactions:
            if transaction["ticker"] == ticker:
                if transaction["type"] == "buy":
                    quantity += transaction["quantity"]
                elif transaction["type"] == "sell":
                    quantity -= transaction["quantity"]
        return quantity                            

    # parameters: N/A
    # return: 0
    # action: prints out transaction history (Type, Quantity, Time, Price)
    def printTransactions(self):
        # loop through the transactions and prints in desired format
        for transaction in self.transactions:
            print(f'Type: {transaction.type}, Quantity: {transaction.quantity}, Time: {transaction.time}, Price: {transaction.price}')
        return 0
    
    # parameters: N/A
    # return: total value of portfolio
    def totalValue(self):
        # loop through stocks owned, stockAmount * stockPrice
        totalValue = 0 
        for ticker, quantity in self.assets.items():
               price = self._get_stock_price(ticker)
               toal_value += price * quantity                    
        return totalValue
    
# Graphing methods and data visualization
    
    # parameters: string ticker, string start_date, string end_date, int quantity
        # Note: Dates should be in the format of "YYYY-MM-DD" or "YYYY-MM-DD HH:MM:SS"
    # return: 0
    # action: prints earnings vs time graph for that stock
    def stockEarningsVsTime(self, ticker, start_date, end_date, quantity):
        # print changes in earnings over time, etc.
        
        # get stock data
        stock_data = yf.Ticker(ticker).history(start=start_date, end=end_date)
        
        # calculate earnings at each point in time
        earnings = []
        for index, row in stock_data.iterrows():
            # Calculate the earning for the current time point
            earning = row['Close'] * quantity - row['Open'] * quantity
            earnings.append(earning)
        
        # Create a plot of the earnings over time
        plt.plot(stock_data.index, earnings)
        plt.xlabel('Time')
        plt.ylabel('Earnings')
        plt.show()
        
        return 0
    
    # parameters: start and end date
    # return: graph of entire portfolio earnings vs time
    def portfolioEarningsVsTime(self, start_date, end_date):
        # TODO: Define totalValue() as a function of start and end date, default start and end date is entire period of buying/selling
        return 0









# testing

portfolio = Portfolio()

# Create a new stock object using yfinance
stock1 = Stock(yf_ticker='AAPL')

# Purchase 100 shares of the stock
portfolio.buy('AAPL', 100)

# Check the current value of the portfolio
print(portfolio.totalValue())

# Sell 50 shares of the stock
portfolio.sell('AAPL', 50)

# Check the current value of the portfolio
print(portfolio.totalValue())

# print the transactions
portfolio.printTransactions()

# Get the stock's opening price for the last 5 days
print(stock1.get_opening_price(start_date= '2021-08-01', end_date= '2021-08-05'))

# Get the stock's closing price for the last 5 days
print(stock1.get_closing_price(start_date= '2021-08-01', end_date= '2021-08-05'))

# Get the stock's volume for the last 5 days
print(stock1.get_volume(start_date= '2021-08-01', end_date= '2021-08-05'))
