def decide_scaling(cpu_usage: float) -> str:
    if cpu_usage > 10:      # lowered for testing
        return "SCALE_UP"
    elif cpu_usage < 5:
        return "SCALE_DOWN"
    else:
        return "STABLE"
