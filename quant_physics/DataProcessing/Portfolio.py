import pandas as pd
import json
import matplotlib.pyplot as plt

class Portfolio:
    '''
    Attributes
    '''
    transactionArray = []  # array of Transaction objects
    assetsSet = set([])
    '''
    Methods
    '''
    
    # input: filename
    # output: writes to file
    def exportJSON(filename):
        # store the transactions and assets in a JSON object
        json_data = json.dumps({
            'transactionArray': self.transactionArray,
            'assetsSet': list(self.assetsSet)
        })

        # write JSON object to file
        with open(filename, 'w') as outfile:
            outfile.write(json_data)
            
        return 0
    
    # input: filename
    # output: portfolio object
    def importJSON(filename):
        # read JSON data from the file
        with open(filename, 'r') as infile:
            json_data = infile.read()
        
        # deserialize JSON data
        data = json.loads(json_data)
        
        # create new Portfolio object with the deserialized data
        portfolio = Portfolio()
        portfolio.transactionArray = data['transactionArray']
        portfolio.assetsSet = set(data['assetsSet'])
        
        return portfolio
    
    def buy(self,ticker, quantity):    
        # update assetsSet
        if ticker in self.assests:
            self.assets[ticker] += quantity
        else:
            self.assets[ticker] = quantity
         self.transactions.append({"type": "buy" ,"ticker: ticker, "quantity": quantity})

        return 0
    
    def sell(name, quantity):
        # update assetsSet
        if ticker in self.assets:
             self.assets[ticker] -= quanity
        else: 
              raise Exception("You do not own any shares of {}".format(ticker))
        self.transactions.append({"type": "sell", "ticker": ticker, "quantity": quantity})                        
        return 0
    
    def stockQuantity(self, ticker):
        # check if name is valid (ticker or name? or both?)
        # loop through transaction history add up (type * quantity)
        return 0
        
    def printTransactions():
        # loop through the transactions and prints in desired format
        for transaction in self.transactionArray:
            print(f'Type: {transaction.type}, Quantity: {transaction.quantity}, Time: {transaction.time}, Price: {transaction.price}')
        return 0
    
    def totalValue():
        # loop through stocks owned, stockAmount * stockPrice
        return 0
    
# Graphing methods and data visualization
    
    # input: stock ticker, start and end date, and quantity
    # output: earnings vs time graph for that stock
    def stockEarningsVsTime(self, ticker, start_date, end_date, quantity):
        # input: ticker, start date, end date, quantity graphed
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
    
    # input: start and end date
    # output: graph of entire portfolio earnings vs time
    def portfolioEarningsVsTime(self, start_date, end_date):
        # TODO: Define totalValue() as a function of start and end date, default start and end date is entire period of buying/selling
        return 0
