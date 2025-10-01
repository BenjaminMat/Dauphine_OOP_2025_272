from __future__ import annotations

import unittest
from datetime import datetime, timedelta


class NegativePriceException(Exception):
    def __init__(self, quote: "Quote"):
        self.quote = quote

    def __str__(self):
        return f"Negative Price Exception for {self.quote}"

class EarlierQuoteDateException(Exception):
    def __init__(self, new_quote_date: datetime, last_quote_date: datetime):
        self.new_quote_date = new_quote_date
        self.last_quote_date = last_quote_date

    def __str__(self):
        return (
            "Earlier Quote Date Exception: "
            f"new quote date {self.new_quote_date.isoformat()} is before "
            f"current last quote date {self.last_quote_date.isoformat()}"
        )


class Quote:
    def __init__(self, date: datetime, price: float):
        self.date = date
        self.price = price

    def __repr__(self):
        return f"Quote(date={self.date!r}, price={self.price!r})"

class FinancialAsset:
    def __init__(self, ticker, quote, currency):
        self.ticker: str = ticker
        self.last_quote: Quote = quote
        self.currency: str = currency
        self.history: [Quote] = []


    def update_last_quote(self, new_quote: Quote):
        try:
            self.__check_quote_for_asset(new_quote)
            self.history.append(self.last_quote)
            self.last_quote = new_quote
        except NegativePriceException as price_exception:
            print(str(price_exception))
            print("Quote has not been updated")
        except EarlierQuoteDateException as date_exception:
            print(date_exception)
            self.history.append(new_quote)
        finally:
            pass


    def __check_quote_for_asset(self, new_quote: Quote):
        if new_quote.price < 0:
            raise NegativePriceException(new_quote)
        if new_quote.date < self.last_quote.date:
            raise EarlierQuoteDateException(new_quote.date, self.last_quote.date)


class TestFinancialAsset(unittest.TestCase):

    def setUp(self):
        self.base_time = datetime(2024, 1, 10, 12, 0, 0)
        self.base_quote = Quote(date=self.base_time, price=175.0)
        self.asset = FinancialAsset("AAPL", self.base_quote, "USD")

    def test_negative_price_raises_and_no_state_changes(self):
        last_quote_before_update = self.asset.last_quote
        start_history_len = len(self.asset.history)
        bad_quote = Quote(date=self.base_time + timedelta(hours=1), price=-0.01)

        self.asset.update_last_quote(bad_quote)

        self.assertIs(self.asset.last_quote, last_quote_before_update)
        self.assertEqual(len(self.asset.history), start_history_len)

    def test_earlier_date_raises_and_is_stored_in_history_without_updating_last(self):
        last_quote_before_update = self.asset.last_quote
        start_history_len = len(self.asset.history)
        earlier_quote = Quote(date=self.base_time - timedelta(days=1), price=180.0)

        self.asset.update_last_quote(earlier_quote)

        self.assertIs(self.asset.last_quote, last_quote_before_update)
        self.assertEqual(len(self.asset.history), start_history_len + 1)
        self.assertEqual(self.asset.history[-1], earlier_quote)

    def test_valid_update_moves_old_last_to_history_and_updates_last_quote(self):
        last_quote_before_update = self.asset.last_quote
        newer_quote = Quote(date=self.base_time + timedelta(hours=1), price=190.0)

        self.asset.update_last_quote(newer_quote)

        self.assertEqual(self.asset.last_quote, newer_quote)
        self.assertEqual(len(self.asset.history), 1)
        self.assertEqual(self.asset.history[-1], last_quote_before_update)


if __name__ == "__main__":
    unittest.main(verbosity=2)
