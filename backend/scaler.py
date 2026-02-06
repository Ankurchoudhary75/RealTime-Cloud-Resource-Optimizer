# scaler.py

current_replicas = 1
MIN_REPLICAS = 1
MAX_REPLICAS = 5

def apply_scaling(decision: str) -> int:
    """
    Simulate scaling action based on optimizer decision
    """
    global current_replicas

    if decision == "SCALE_UP" and current_replicas < MAX_REPLICAS:
        current_replicas += 1

    elif decision == "SCALE_DOWN" and current_replicas > MIN_REPLICAS:
        current_replicas -= 1

    return current_replicas
