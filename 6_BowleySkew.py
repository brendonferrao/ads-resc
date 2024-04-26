import numpy as np
import pandas as pd

data = pd.read_csv("age.csv")

q1, median, q3 = np.percentile(data, [25, 50, 75])
skewness = (q1 + q3 - 2 * median) / (q3 - q1)

print("Bowley's coefficient of skewness:", skewness)
