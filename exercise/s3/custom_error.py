"""
# Create a custom exception named EarlierQuoteDateException that raised an error when the date of a quote used to 
# update last quote for asset is before the current stored quote. The error should indicate the date of the quote used 
# for the update and also the date in the last_quote attribute of the FinancialAssetObject
# Then modify the update_last_quote() to store the quote in the quote history without updating the last quote attribute
"""
import unittest
from datetime import datetime, timedelta


class NegativePriceException(Exception):
    def __init__(self, *args):
        self._args = args

    def __str__(self):
        return f"Negative Price Exception for {self._args}"


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
            # raise
        finally:
            pass

    def __check_quote_for_asset(self, new_quote: Quote):
        if new_quote.price < 0:
            raise NegativePriceException(new_quote)


last_date, last_close = datetime.now(), 175.0
equity_last_quote = Quote(last_date, last_close)
equity = FinancialAsset('AAPL', equity_last_quote, 'USD')

last_date2, last_close2 = datetime.now(), -200
equity_last_quote2 = Quote(last_date2, last_close2)
equity.update_last_quote(equity_last_quote2)


class TestFinancialAsset(unittest.TestCase):

    def setUp(self):
        self.base_time = datetime(2024, 1, 10, 12, 0, 0)
        self.base_quote = Quote(date=self.base_time, price=175.0)
        self.asset = FinancialAsset("AAPL", self.base_quote, "USD")

    def test_negative_price_raises_and_no_state_changes(self):
        last_quote_before_update = self.asset.last_quote
        start_history_len = len(self.asset.history)
        bad_quote = Quote(date=self.base_time + timedelta(hours=1), price=-0.01)

        with self.assertRaises(NegativePriceException) as ctx:
            self.asset.update_last_quote(bad_quote)

        self.assertIn("Negative Price Exception", str(ctx.exception))
        self.assertIs(self.asset.last_quote, last_quote_before_update)
        self.assertEqual(len(self.asset.history), start_history_len)

    def test_earlier_date_raises_and_is_stored_in_history_without_updating_last(self):
        last_quote_before_update = self.asset.last_quote
        start_history_len = len(self.asset.history)
        earlier_quote = Quote(date=self.base_time - timedelta(days=1), price=180.0)

        with self.assertRaises(EarlierQuoteDateException) as ctx:
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
