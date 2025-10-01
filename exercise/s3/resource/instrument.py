import pandas as pd

from exercise.s3.resource.quote import Quote


class Instrument:
    def __init__(self, ticker: str, exchange: str, quote: Quote, currency: str):
        self.ticker: str = ticker
        self.exchange: str = exchange
        self.last_quote: Quote = quote
        self.currency: str = currency
        self.quote_history: [Quote] = []

    def __str__(self):
        print(f'Instrument with ticker {self.ticker}, currency {self.currency} and last quote {self.last_quote}')

    def update_price(self, new_quote: Quote):
        self.quote_history.append(self.last_quote)
        self.last_quote = new_quote

    def populate_quote_history_from_df(self, df_data: pd.DataFrame):
        dates = df_data.index.to_pydatetime().tolist()
        prices = df_data['Close'].tolist()
        self.quote_history = [Quote(date, price) for date, price in zip(dates, prices)]

    def quotes_to_dataframe(self) -> pd.DataFrame:
        data = {
            "Date": [quote.date for quote in self.quote_history],
            "Price": [quote.price for quote in self.quote_history]
        }
        df = pd.DataFrame(data)
        df.set_index('Date', inplace=True)
        return df
