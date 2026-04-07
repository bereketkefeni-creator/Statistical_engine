from typing import List, Union
import math
from collections import Counter

Number = Union[int, float]

class StatEngine:
    def __init__(self, data: List[Number]):
        if not data:
            raise ValueError("Data list is empty")

        # Clean data: keep only numeric values
        self.data = [x for x in data if isinstance(x, (int, float))]
        if not self.data:
            raise TypeError("No valid numeric data found")

        self.n = len(self.data)

    def get_mean(self) -> float:
        return sum(self.data) / self.n

    def get_median(self) -> float:
        sorted_data = sorted(self.data)
        mid = self.n // 2

        if self.n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        return sorted_data[mid]

    def get_mode(self):
        counts = Counter(self.data)
        max_freq = max(counts.values())

        if max_freq == 1:
            return "All values are unique; no mode"

        return [k for k, v in counts.items() if v == max_freq]

    def get_variance(self, is_sample=True) -> float:
        mean = self.get_mean()
        squared_diffs = [(x - mean) ** 2 for x in self.data]
        total = sum(squared_diffs)

        if is_sample:
            if self.n < 2:
                raise ValueError("Sample variance requires at least 2 data points")
            return total / (self.n - 1)

        return total / self.n

    def get_standard_deviation(self, is_sample=True) -> float:
        return math.sqrt(self.get_variance(is_sample))

    def get_outliers(self, threshold=2):
        mean = self.get_mean()
        std_dev = self.get_standard_deviation()

        return [x for x in self.data if abs(x - mean) > threshold * std_dev]
