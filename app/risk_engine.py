def compute_risk_score(state):

    risk = (
        0.35 * state["CLI"]
        + 0.30 * state["CEI"]
        + 0.20 * state["NODI"]
        + 0.15 * state["WBI"]
    )

    return round(risk, 3)


def classify_risk(score):

    if score < 0.4:
        return "NORMAL"

    if score < 0.7:
        return "ELEVATED"

    return "CRITICAL"


def compute_risk(state):

    score = compute_risk_score(state)

    return {
        "risk_score": score,
        "risk_level": classify_risk(score)
    }