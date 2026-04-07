import json
from src.stat_engine import StatEngine
from src.monte_carlo import simulate_crashes

def main():
    # Load salary data
    with open("data/sample_salaries.json") as f:
        salaries = json.load(f)

    engine = StatEngine(salaries)

    print("=== Salary Statistics ===")
    print("Mean:", engine.get_mean())
    print("Median:", engine.get_median())
    print("Mode:", engine.get_mode())

    print("\n--- Variance & Standard Deviation ---")
    print("Sample Variance:", engine.get_variance(is_sample=True))
    print("Population Variance:", engine.get_variance(is_sample=False))
    print("Sample Std Dev:", engine.get_standard_deviation(True))
    print("Population Std Dev:", engine.get_standard_deviation(False))

    print("\n--- Outliers ---")
    print(engine.get_outliers(threshold=2))

    print("\n=== Monte Carlo Simulation ===")
    for days in [30, 365, 10000]:
        prob = simulate_crashes(days)
        print(f"{days} days → Crash Probability: {prob:.4f}")

if __name__ == "__main__":
    main()
