import numpy as np
import pandas as pd

data = pd.read_csv("gym.csv")
x=data['Age']
y=data['Fitness']

rank_x = np.argsort(x).argsort() + 1
rank_y = np.argsort(y).argsort() + 1
differences = rank_x - rank_y
n = len(x)
spearman_corr = 1 - (6 * np.sum(differences**2)) / (n * (n**2 - 1))

print("Spearman's correlation coefficient:", spearman_corr)
