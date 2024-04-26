import numpy as np
import pandas as pd

data = pd.read_csv("gym.csv")
x=data['Age']
y=data['Fitness']
mean_x = np.mean(x)
mean_y = np.mean(y)

numerator = np.sum((x - mean_x) * (y - mean_y))
denominator = np.sqrt(np.sum((x - mean_x)**2) * np.sum((y - mean_y)**2))
pearson_corr = numerator / denominator

print("Karl Pearson's correlation coefficient:", pearson_corr)
