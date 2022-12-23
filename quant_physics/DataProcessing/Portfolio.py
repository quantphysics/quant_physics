import pandas as pd


class Portfolio:
    '''
    Attributes
    '''
    transactionArray = []  # array of Transaction objects
    assetsSet = set([])
    '''
    Methods
    '''
    def exportJSON(filename):
        # input: name of file
        # output: write to desired file
        return 0
        
    def importJSON(filename):
        # input: filename or path
        # output: ???
        return 0
    
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
        # loops through transactionsArray and prints in desired format
        return 0
    
    def totalValue():
        # loop through stocks owned, stockAmount * stockPrice
        return 0
    
    # Graphing methods and data visualization
    def printEarningsVsTime():
        # input: ticker, start date, end date, quantity graphed
        # print changes in earnings over time, etc.
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
        
        