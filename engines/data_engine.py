# --------------------------------
# PREDICTRON V2 DATA ENGINE
# --------------------------------

import yfinance as yf

import numpy as np


def fetch_company_data(ticker):

    try:

        stock = yf.Ticker(ticker)

        info = stock.info

        fast = stock.fast_info

        hist = stock.history(
            period="3mo"
        )

        # --------------------------------
        # 30D MOMENTUM
        # --------------------------------

        if len(hist) >= 22:

            start_price = hist[
                "Close"
            ].iloc[-22]

            end_price = hist[
                "Close"
            ].iloc[-1]

            thirty_day_return = (

                (
                    end_price
                    -
                    start_price
                )

                /

                start_price

            ) * 100

        else:

            thirty_day_return = 0

        # --------------------------------
        # VOLATILITY
        # --------------------------------

        daily_returns = (

            hist["Close"]

            .pct_change()

            .dropna()
        )

        volatility = np.std(
            daily_returns
        ) * 100

        return {

            "ticker":
                ticker,

            "market_cap":
                fast.get(
                    "marketCap",
                    0
                ),

            "current_price":
                fast.get(
                    "lastPrice",
                    0
                ),

            "revenue_growth":
                info.get(
                    "revenueGrowth",
                    0
                ) or 0,

            "profit_margins":
                info.get(
                    "profitMargins",
                    0
                ) or 0,

            "thirty_day_return":
                thirty_day_return,

            "volatility":
                volatility
        }

    except Exception as e:

        print(
            f"\nFailed fetching {ticker}"
        )

        print(e)

        return None