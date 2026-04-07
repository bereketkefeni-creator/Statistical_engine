import random
def simulate_crashes(days: int, crash_prob=0.045) -> float:
    if days <= 0:
        raise ValueError("Days must be positive")
    crashes = 0
    for _ in range(days):
        if random.random() < crash_prob:
            crashes += 1
    return crashes / days