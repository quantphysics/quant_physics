import json

class Transaction:
    # create constructor so we can read in as JSON
    def __init__(self, data):
        self.type = data['type']
        self.quantity = data['quantity']
        self.time = data['time']
        self.price = data['price']
        self.ticker = data['ticker']

    # create dictionary method so we can export as JSON
    def __dict__(self):
        return {
            'type': self.type,
            'quantity': self.quantity,
            'time': self.time,
            'price': self.price,
            'ticker': self.ticker
        }
