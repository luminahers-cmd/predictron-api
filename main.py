# --------------------------------
# PREDICTRON V2 QUANT SYSTEM
# --------------------------------

import pandas as pd

from datetime import datetime

from config import TICKERS

from engines.data_engine import (
    fetch_company_data
)

from engines.feature_engine import (
    build_features
)

from engines.model_engine import (
    calculate_scores
)

from engines.backtest_engine import (
    calculate_future_return
)

from engines.analytics_engine import (
    analyze_history
)

from engines.portfolio_engine import (
    simulate_portfolio
)

print("\n=== PREDICTRON V2 MULTI-HORIZON SYSTEM ===\n")

results = []

for ticker in TICKERS:

    print(f"\nAnalyzing: {ticker}")

    raw_data = fetch_company_data(
        ticker
    )

    if raw_data:

        features = build_features(
            raw_data
        )

        scores = calculate_scores(
            features
        )

        future_return = (
            calculate_future_return(
                ticker
            )
        )

        timestamp = datetime.now()

        result = {

            "timestamp":
                timestamp,

            "ticker":
                ticker,

            "long_term":
                scores[
                    "long_term_score"
                ],

            "short_term":
                scores[
                    "short_term_score"
                ],

            "combined":
                scores[
                    "combined_score"
                ],

            "future_return":
                future_return
        }

        results.append(result)

        print("\nFEATURES:")
        print(features)

        print("\nSCORES:")
        print(scores)

        print(
            f"\n30D RETURN: "
            f"{future_return}%"
        )

    else:

        print(
            f"Failed fetching {ticker}"
        )

# --------------------------------
# COMBINED RANKINGS
# --------------------------------

print("\n=== COMBINED RANKINGS ===\n")

combined_sorted = sorted(

    results,

    key=lambda x: x["combined"],

    reverse=True
)

for result in combined_sorted:

    print(

        f"{result['ticker']}"

        f" | LT: "

        f"{result['long_term']}"

        f" | ST: "

        f"{result['short_term']}"

        f" | COMBINED: "

        f"{result['combined']}"

        f" | RETURN: "

        f"{result['future_return']}%"
    )

# --------------------------------
# VALIDATION
# --------------------------------

top_half = combined_sorted[:4]

bottom_half = combined_sorted[4:]

top_avg = sum(

    x["future_return"]

    for x in top_half

) / len(top_half)

bottom_avg = sum(

    x["future_return"]

    for x in bottom_half

) / len(bottom_half)

print("\n=== VALIDATION ===\n")

print(
    f"Top-half avg return: "
    f"{round(top_avg,2)}%"
)

print(
    f"Bottom-half avg return: "
    f"{round(bottom_avg,2)}%"
)

if top_avg > bottom_avg:

    print(
        "\nPredictron ranking "
        "shows positive signal."
    )

else:

    print(
        "\nPredictron ranking "
        "needs improvement."
    )

# --------------------------------
# SAVE HISTORY
# --------------------------------

history_df = pd.DataFrame(
    results
)

history_df.to_csv(

    "data/prediction_history.csv",

    mode="a",

    header=False,

    index=False
)

print(
    "\nPrediction history saved."
)

# --------------------------------
# ANALYTICS
# --------------------------------

analyze_history()

# --------------------------------
# PORTFOLIO SIMULATION
# --------------------------------

simulate_portfolio(
    combined_sorted
)

print("\nSystem Complete.")