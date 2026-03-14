import numpy as np


def compute_confidence(state):

    values = np.array([
        state["CEI"],
        state["CLI"],
        state["NODI"],
        state["WBI"]
    ])

    variance = np.var(values)

    confidence = 1 - min(variance, 1)

    return round(float(confidence), 3)


def classify_confidence(score):

    if score > 0.75:
        return "HIGH"

    if score > 0.5:
        return "MEDIUM"

    return "LOW"


def compute_confidence_state(state):

    score = compute_confidence(state)

    return {
        "confidence_score": score,
        "confidence_mode": classify_confidence(score)
    }