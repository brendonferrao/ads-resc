import numpy as np
import pandas as pd

data = pd.read_csv("age.csv")

skewness = np.mean((data - np.mean(data))**3) / np.std(data)**3
kurtosis = np.mean((data - np.mean(data))**4) / np.std(data)**4 - 3

print("Using NumPy:")
print("Skewness:", skewness)
print("Kurtosis:", kurtosis)
