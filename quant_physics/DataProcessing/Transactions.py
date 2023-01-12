import json

class Transaction:
    type = ""  # "buy" or "sell"
    quantity = 0
    time = ""  # Time you bought asset: Pandas Series .index should give date
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
