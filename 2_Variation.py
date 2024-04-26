import numpy as np
import pandas as pd

data = pd.read_csv("age.csv")

series = data.stack()
range_pd = series.max() - series.min()
iqr_pd = series.quantile(0.75) - series.quantile(0.25)
variance_pd = series.var()
std_deviation_pd = series.std()
coefficient_variation_pd = (std_deviation_pd / series.mean()) * 100

print("Range:",f"{series.min()}-{series.max()} ({range_pd})")
print("Interquartile Range:", int(iqr_pd))
print("Variance:", variance_pd)
print("Standard Deviation:", std_deviation_pd)
print("Coefficient of Variation:", coefficient_variation_pd)
