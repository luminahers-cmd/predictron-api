# --------------------------------
# PREDICTRON V2 DASHBOARD
# --------------------------------

import streamlit as st

import pandas as pd

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

# --------------------------------
# PAGE CONFIG
# --------------------------------

st.set_page_config(

    page_title="Predictron V2",

    layout="wide"
)

# --------------------------------
# TITLE
# --------------------------------

st.title(
    "🚀 Predictron V2 Quant Dashboard"
)

st.write(
    "Live multi-factor market intelligence system."
)

results = []

# --------------------------------
# RUN MODEL
# --------------------------------

for ticker in TICKERS:

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

        results.append({

            "Ticker":
                ticker,

            "Long-Term":
                scores[
                    "long_term_score"
                ],

            "Short-Term":
                scores[
                    "short_term_score"
                ],

            "Combined":
                scores[
                    "combined_score"
                ],

            "Volatility":
                features[
                    "volatility"
                ],

            "Momentum":
                features[
                    "momentum_score"
                ],

            "Quality":
                features[
                    "quality_score"
                ],

            "Execution":
                features[
                    "execution_score"
                ]
        })

# --------------------------------
# DATAFRAME
# --------------------------------

df = pd.DataFrame(
    results
)

# --------------------------------
# HANDLE EMPTY DATA
# --------------------------------

if df.empty:

    st.error(
        "No stock data loaded."
    )

else:

    # --------------------------------
    # SORT
    # --------------------------------

    df = df.sort_values(

        by="Combined",

        ascending=False
    )

    # --------------------------------
    # DISPLAY TABLE
    # --------------------------------

    st.subheader(
        "📊 Live Rankings"
    )

    st.dataframe(

        df,

        use_container_width=True
    )

    # --------------------------------
    # TOP PICK
    # --------------------------------

    top_pick = df.iloc[0]

    st.subheader(
        "🏆 Top Ranked Stock"
    )

    st.success(

        f"{top_pick['Ticker']} "

        f"| Combined Score: "

        f"{round(top_pick['Combined'],2)}"
    )

    # --------------------------------
    # METRICS
    # --------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(

            "Top Combined Score",

            round(
                df["Combined"].max(),
                2
            )
        )

    with col2:

        st.metric(

            "Average Volatility",

            round(
                df["Volatility"].mean(),
                2
            )
        )

    with col3:

        st.metric(

            "Average Momentum",

            round(
                df["Momentum"].mean(),
                2
            )
        )