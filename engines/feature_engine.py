# --------------------------------
# PREDICTRON V2 FEATURE ENGINE
# --------------------------------

import math


def build_features(raw_data):

    market_cap = raw_data[
        "market_cap"
    ]

    current_price = raw_data[
        "current_price"
    ]

    revenue_growth = raw_data.get(
        "revenue_growth",
        0
    )

    profit_margins = raw_data.get(
        "profit_margins",
        0
    )

    thirty_day_return = raw_data.get(
        "thirty_day_return",
        0
    )

    volatility = raw_data.get(
        "volatility",
        0
    )

    # --------------------------------
    # QUALITY
    # --------------------------------

    quality_score = max(

        0,

        min(

            100,

            (

                (revenue_growth * 100)

                +

                (profit_margins * 120)

            )
        )
    )

    # --------------------------------
    # MOMENTUM
    # --------------------------------

    momentum_score = max(

        0,

        min(

            100,

            (
                thirty_day_return * 4
            )

            +

            (
                math.sqrt(
                    current_price
                ) * 2
            )
        )
    )

    # --------------------------------
    # MOAT
    # --------------------------------

    moat_score = min(

        100,

        math.log10(
            market_cap + 1
        ) * 8
    )

    # --------------------------------
    # RISK
    # --------------------------------

    volatility_penalty = min(
        50,
        volatility * 8
    )

    risk_score = max(

        0,

        100

        -

        volatility_penalty

        -

        (
            abs(profit_margins)
            * 50
        )
    )

    # --------------------------------
    # EXECUTION
    # --------------------------------

    execution_score = (

        quality_score * 0.20

        +

        momentum_score * 0.50

        +

        moat_score * 0.15

        +

        risk_score * 0.15
    )

    return {

        "quality_score":
            round(
                quality_score,
                2
            ),

        "momentum_score":
            round(
                momentum_score,
                2
            ),

        "moat_score":
            round(
                moat_score,
                2
            ),

        "risk_score":
            round(
                risk_score,
                2
            ),

        "volatility":
            round(
                volatility,
                2
            ),

        "execution_score":
            round(
                execution_score,
                2
            )
    }