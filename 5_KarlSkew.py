import numpy as np
import pandas as pd

data = pd.read_csv("age.csv")

mean = np.mean(data)
median = np.median(data)
std_deviation = np.std(data)
skewness = list(3 * (mean - median) / std_deviation)

print("Karl Pearson's coefficient of skewness:", *skewness)
