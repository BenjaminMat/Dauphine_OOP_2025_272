from datetime import datetime


class Quote:
    def __init__(self, date: datetime, price: float):
        self.date = date
        self.price = price

    def __str__(self):
        return f'(date: {self.date}, price: {self.price})'
