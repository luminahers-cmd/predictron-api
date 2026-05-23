# --------------------------------
# PREDICTRON V2 ANALYTICS ENGINE
# --------------------------------

import pandas as pd


def analyze_history():

    try:

        df = pd.read_csv(
            "data/prediction_history.csv",

            names=[

                "timestamp",

                "ticker",

                "long_term",

                "short_term",

                "combined",

                "future_return"
            ]
        )

        print(
            "\n=== HISTORICAL ANALYTICS ===\n"
        )

        # --------------------------------
        # TOP PERFORMERS
        # --------------------------------

        top_companies = (

            df.groupby(
                "ticker"
            )["future_return"]

            .mean()

            .sort_values(
                ascending=False
            )
        )

        print(
            "Average Returns By Ticker:\n"
        )

        print(
            top_companies
        )

        # --------------------------------
        # BEST MODEL SCORES
        # --------------------------------

        avg_combined = df[
            "combined"
        ].mean()

        avg_return = df[
            "future_return"
        ].mean()

        print(
            "\nAverage Combined Score:"
        )

        print(
            round(
                avg_combined,
                2
            )
        )

        print(
            "\nAverage Future Return:"
        )

        print(
            round(
                avg_return,
                2
            )
        )

    except Exception as e:

        print(
            "\nAnalytics failed."
        )

        print(e)