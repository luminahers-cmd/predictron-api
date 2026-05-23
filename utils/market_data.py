import yfinance as yf


def fetch_stock_data(ticker):

    data = yf.download(

        ticker,

        period="6mo",

        interval="1d"

    )

    return data


if __name__ == "__main__":

    nvda = fetch_stock_data("NVDA")

    print(nvda.tail())