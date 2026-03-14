def fallback_dispatch_rule(state):
    if state["CEI"] > 1.0 and state["CLI"] > 0.15:
        return (
            "Fallback rule activated: assign the nearest available courier "
            "with the lowest active delivery load and temporarily rebalance "
            "dispatch coverage in overloaded zones."
        )

    if state["WBI"] > 0.9:
        return (
            "Fallback rule activated: prioritize urgent orders, queue normal orders, "
            "and reduce dispatch congestion by redistributing outbound load."
        )

    return (
        "Fallback rule activated: assign the nearest available courier "
        "with the lowest active delivery load."
    )


def build_recommendation(state, risk, confidence):
    mode = confidence["confidence_mode"]

    if mode == "HIGH":
        return {
            "decision_mode": "AI_RECOMMENDATION",
            "recommendation": (
                "AI recommendation: Zone operations are stable enough for AI-assisted "
                "dispatch optimization. Reallocate courier capacity toward the highest-risk zone "
                "and monitor lateness propagation over the next 60 minutes."
            )
        }

    if mode == "MEDIUM":
        return {
            "decision_mode": "AI_ADVISORY",
            "recommendation": (
                "AI advisory: Operational stress is rising. Consider adding temporary courier "
                "coverage in overloaded zones and prioritizing urgent pharmacy deliveries."
            )
        }

    return {
        "decision_mode": "FALLBACK_RULE",
        "recommendation": fallback_dispatch_rule(state)
    }