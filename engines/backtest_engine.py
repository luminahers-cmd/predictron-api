import yfinance as yf

import pandas as pd

import numpy as np


def backtest_strategy(

    ticker="NVDA",

    period="1y"

):

    data = yf.download(

        ticker,

        period=period,

        interval="1d"

    )


    data["Returns"] = (

        data["Close"].pct_change()

    )


    data["Cumulative"] = (

        1 + data["Returns"]

    ).cumprod()


    total_return = (

        data["Cumulative"].iloc[-1] - 1

    ) * 100


    volatility = (

        data["Returns"].std()

        * np.sqrt(252)

        * 100

    )


    sharpe = (

        data["Returns"].mean()

        / data["Returns"].std()

    ) * np.sqrt(252)


    max_drawdown = (

        (

            data["Cumulative"]

            /

            data["Cumulative"].cummax()

        ) - 1

    ).min() * 100


    results = {

        "ticker": ticker,

        "total_return": round(

            total_return,

            2

        ),

        "volatility": round(

            volatility,

            2

        ),

        "sharpe_ratio": round(

            sharpe,

            2

        ),

        "max_drawdown": round(

            max_drawdown,

            2

        )

    }


    return results


if __name__ == "__main__":

    result = backtest_strategy(

        "NVDA"

    )

    print(result)