
def check_critical_proximity(distance):
    """
    Trigger safety interrupt when obstacle
    is within critical proximity.
    """

    return distance <= 1.0
