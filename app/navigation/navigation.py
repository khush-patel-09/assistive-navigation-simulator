
def get_navigation_action(distance, risk_level):
    """
    Basic obstacle avoidance navigation.
    """

    # Critical proximity safety interrupt
    if distance <= 1.0:
        return "STOP"

    if risk_level == "Critical":
        return "MOVE LEFT"

    elif risk_level == "Caution":
        return "PROCEED SLOWLY"

    return "MOVE FORWARD"
