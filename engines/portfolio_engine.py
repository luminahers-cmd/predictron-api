# --------------------------------
# PREDICTRON V2 PORTFOLIO ENGINE
# --------------------------------

def simulate_portfolio(results):

    try:

        # --------------------------------
        # SORT BY COMBINED SCORE
        # --------------------------------

        sorted_results = sorted(

            results,

            key=lambda x: x[
                "combined"
            ],

            reverse=True
        )

        # --------------------------------
        # TOP 3 PICKS
        # --------------------------------

        top_picks = sorted_results[:3]

        portfolio_return = sum(

            stock[
                "future_return"
            ]

            for stock in top_picks

        ) / len(top_picks)

        print(
            "\n=== PORTFOLIO SIMULATION ===\n"
        )

        print(
            "Top Portfolio Picks:\n"
        )

        for stock in top_picks:

            print(

                f"{stock['ticker']}"

                f" | Score: "

                f"{stock['combined']}"

                f" | Return: "

                f"{stock['future_return']}%"
            )

        print(

            f"\nSimulated Portfolio Return: "

            f"{round(portfolio_return,2)}%"
        )

    except Exception as e:

        print(
            "\nPortfolio simulation failed."
        )

        print(e)