# --------------------------------
# PREDICTRON V2 API
# --------------------------------

from fastapi import FastAPI

from fastapi.middleware.cors import (
    CORSMiddleware
)

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

app = FastAPI()

# --------------------------------
# CORS
# --------------------------------

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

# --------------------------------
# ROOT
# --------------------------------

@app.get("/")

def root():

    return {

        "message":
            "Predictron API Running"
    }

# --------------------------------
# RANKINGS
# --------------------------------

@app.get("/rankings")

def get_rankings():

    results = []

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

                "volatility":
                    features[
                        "volatility"
                    ],

                "momentum":
                    features[
                        "momentum_score"
                    ]
            })

    sorted_results = sorted(

        results,

        key=lambda x: x[
            "combined"
        ],

        reverse=True
    )

    return sorted_results