import numpy as np
import pandas as pd

data = pd.read_csv("age.csv")

mean = np.mean(data)
median = np.median(data)
quartiles = np.percentile(data, [25, 50, 75])
series = data.stack()
mode = series.mode()
percentiles = list(series.quantile([0.25, 0.5, 0.75]))

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode[0])
print("Quartiles (Q1, Q2, Q3):", *[int(q) for q in quartiles])
print("Percentiles (25th, 50th, 75th):", *[int(p) for p in percentiles])
