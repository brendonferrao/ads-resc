import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('useless.csv')

print("Null values before prepocessing: ")
print(df.isnull().sum())
df.fillna({'Age': df['Age'].median(), 'Income': df['Income'].median(), 'Education': 'Not Provided'}, inplace=True)
print("\nNull values after prepocessing: ")
print(df.isnull().sum())

print("\nDuplicate values before prepocessing: ")
print(df.duplicated().sum())
df.drop_duplicates(subset='Name', keep='first', inplace=True)
print("Duplicate values after prepocessing: ")
print(df.duplicated().sum())

plt.figure(figsize=(10, 3))
plt.subplot(2,2,1)
plt.boxplot(df['Income'], vert=False, showfliers=True)
plt.title('Box Plot of Income')
plt.ylabel('Income')

Q1 = df['Income'].quantile(0.25)
Q3 = df['Income'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df['Income'] = np.where(df['Income'] < lower_bound, lower_bound, df['Income'])
df['Income'] = np.where(df['Income'] > upper_bound, upper_bound, df['Income'])

plt.subplot(2,2,2)
plt.boxplot(df['Income'], vert=False, showfliers=True)
plt.title('Box Plot of Income: After Outlier Removal')
plt.ylabel('Income')

plt.tight_layout()
plt.show()
