
def calculate_risk(visual_confidence, distance):
    """
    Combine visual confidence and simulated distance
    into an obstacle risk score between 0 and 1.
    """

    distance_confidence = max(0, min(1, 1 - distance / 5))

    risk_score = (
        0.6 * visual_confidence
        + 0.4 * distance_confidence
    )

    return round(risk_score, 2)


def classify_risk(risk_score):
    if risk_score >= 0.7:
        return "Critical"
    elif risk_score >= 0.4:
        return "Caution"
    else:
        return "Safe"
