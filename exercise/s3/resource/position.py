from datetime import datetime

from exercise.s3.resource.instrument import Instrument


class Position:
    def __init__(self, instrument: Instrument, date: datetime = datetime.now(), weight: float = 0, quantity: float = 0):
        self.instrument = instrument
        self.date = date
        self.weight = weight
        self.quantity = quantity

    def update(self, date: datetime, weight: float, quantity: float):
        if date is not None:
            self.date = date
        if weight is not None:
            self.weight = weight
        if quantity is not None:
            self.quantity = quantity