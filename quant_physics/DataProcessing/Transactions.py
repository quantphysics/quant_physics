import json
from transactions import Transaction

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
