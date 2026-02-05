def decide_scaling(cpu_usage: float) -> str:
    """
    Decide scaling action based on CPU usage
    """
    if cpu_usage > 70:
        return "SCALE_UP"
    elif cpu_usage < 30:
        return "SCALE_DOWN"
    else:
        return "STABLE"
