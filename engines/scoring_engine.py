from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from engines.scoring_engine import calculate_scores


app = FastAPI()


app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)


@app.get("/")

def root():

    return {

        "message": "Predictron API Running"

    }


@app.get("/rankings")

def get_rankings():

    tickers = [

        "NVDA",

        "AAPL",

        "MSFT",

        "TSLA",

        "META"

    ]

    results = []

    for ticker in tickers:

        try:

            score = calculate_scores(ticker)

            results.append(score)

        except Exception as e:

            print(f"Error with {ticker}: {e}")

    sorted_results = sorted(

        results,

        key=lambda x: x["combined"],

        reverse=True

    )

    return sorted_results