# Statistical Engine & Monte Carlo Simulation

## Project Overview
This project implements a pure Python statistical engine (`StatEngine`) for analyzing 1D numerical data, including central tendency, variance, standard deviation, and outlier detection. It also demonstrates the Law of Large Numbers via a Monte Carlo simulation of server failures.

## Mathematical Logic
- **Mean**: sum(data) / n  
- **Median**: middle value of sorted data (average of middle two if even length)  
- **Mode**: most frequent value(s), supports multimodal distributions  
- **Variance**:  
  - Sample variance: sum((x - mean)^2) / (n - 1)  
  - Population variance: sum((x - mean)^2) / n  
- **Standard Deviation**: sqrt(variance)  
- **Outliers**: values > threshold * std deviation away from mean

## Setup Instructions
1. Clone this repo:
   ```bash
   git clone <your-repo-url>
   cd statistical_engine
