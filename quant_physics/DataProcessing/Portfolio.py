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
    
    def buy(name, quantity):    
        # update assetsSet
        return 0
    
    def sell(name, quantity):
        # update assetsSet
        return 0
    
    def stockQuantity(name):
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

    # nested class for transactions
    class Transaction:
        type = 0
        '''
        “purchase” = +1
        “sell” = -1
        Note: this will make calculations much easier, e.g. to add up total amount of a stock, just add up all values of (type * quantity) without need for if statements
        '''
        quantity = 0
        time = 0  # Time you bought asset: Pandas Series .index should give date
        price = 0
        
        # create constructor so we can read in as JSON
        def __init__(self, data):
            self.type = data['type']
            self.quantity = data['quantity']
            self.time = data['time']
            self.price = data['price']
            
        # create dictionary method so we can export as JSON
        def __dict__(self):
            return {
                'type': self.type,
                'quantity': self.quantity,
                'time': self.time,
                'price': self.price
            }
        
        
