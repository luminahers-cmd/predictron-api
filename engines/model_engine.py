# --------------------------------
# PREDICTRON V2 MODEL ENGINE
# --------------------------------

def calculate_scores(features):

    quality_score = features[
        "quality_score"
    ]

    momentum_score = features[
        "momentum_score"
    ]

    moat_score = features[
        "moat_score"
    ]

    risk_score = features[
        "risk_score"
    ]

    execution_score = features[
        "execution_score"
    ]

    # --------------------------------
    # LONG-TERM MODEL
    # --------------------------------

    long_term_score = (

        quality_score * 0.35

        +

        moat_score * 0.35

        +

        risk_score * 0.15

        +

        execution_score * 0.15
    )

    # --------------------------------
    # SHORT-TERM MODEL
    # --------------------------------

    short_term_score = (

        momentum_score * 0.55

        +

        execution_score * 0.25

        +

        risk_score * 0.20
    )

    # --------------------------------
    # COMBINED MODEL
    # --------------------------------

    combined_score = (

        long_term_score * 0.35

        +

        short_term_score * 0.65
    )

    return {

        "long_term_score":
            round(
                long_term_score,
                2
            ),

        "short_term_score":
            round(
                short_term_score,
                2
            ),

        "combined_score":
            round(
                combined_score,
                2
            )
    }